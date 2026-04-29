"""
太阳系角动量计算器
  ① 八大行星轨道角动量  L = m · (r × v)
  ② 太阳自转角动量      L_☉ = I_☉ · ω_☉ · n̂
  ③ 矢量总和及大小

参考系：ICRF 赤道坐标系（J2000.0），以太阳质心为原点
数据源：NASA JPL Horizons System（行星状态向量 + 太阳物理参数全部在线拉取）

依赖安装：
    pip install astroquery astropy numpy requests
"""

import re
import sys
import requests
import numpy as np
from astropy.time import Time
from astroquery.jplhorizons import Horizons

# ══════════════════════════════════════════════════════════════════════
# 全局常量
# ══════════════════════════════════════════════════════════════════════

G             = 6.67430e-11           # 万有引力常数  m³ kg⁻¹ s⁻²
AU_TO_M       = 1.495978707e11        # 1 AU → m
AU_DAY_TO_MPS = AU_TO_M / 86400.0    # AU/day → m/s
EPOCH         = Time("2025-01-01").jd # 查询历元（Julian Date）


PLANETS = [
    {"name": "水星 Mercury",   "id": "199", "mass_kg": 3.3011e23},
    {"name": "金星 Venus",     "id": "299", "mass_kg": 4.8675e24},
    {"name": "地球 Earth",     "id": "399", "mass_kg": 5.9724e24},
    {"name": "火星 Mars",      "id": "499", "mass_kg": 6.4171e23},
    {"name": "木星 Jupiter",   "id": "599", "mass_kg": 1.8982e27},
    {"name": "土星 Saturn",    "id": "699", "mass_kg": 5.6834e26},
    {"name": "天王星 Uranus",  "id": "799", "mass_kg": 8.6810e25},
    {"name": "海王星 Neptune", "id": "899", "mass_kg": 1.0241e26},
]


# ══════════════════════════════════════════════════════════════════════
# 从 JPL Horizons API 拉取太阳物理参数
# ══════════════════════════════════════════════════════════════════════

def fetch_sun_params() -> dict:
    """
    查询 JPL Horizons 获取太阳物理参数：
      - GM → 质量 M_☉
      - 平均半径 R_☉
      - 恒星自转周期 T_☉
      - 自转轴方向（北极 RA、Dec，ICRF 赤道系）
    返回 SI 单位。
    """
    url = "https://ssd.jpl.nasa.gov/api/horizons.api"
    payload = {
        "format":     "text",
        "COMMAND":    "10",   # 太阳 JPL ID
        "OBJ_DATA":   "YES",
        "MAKE_EPHEM": "NO",
    }
    resp = requests.get(url, params=payload, timeout=20)
    resp.raise_for_status()
    text = resp.text

    def parse(pattern, cast=float, flags=re.IGNORECASE):
        m = re.search(pattern, text, flags)
        if not m:
            raise ValueError(f"未能在 Horizons 响应中找到匹配：{pattern}")
        return cast(m.group(1))

    # GM (km³/s²) → m³/s² → 质量 (kg)
    gm_km3 = parse(r"GM\s*[,=]\s*([\d.]+(?:[eE][+\-]?\d+)?)")
    gm_m3  = gm_km3 * 1e9
    mass   = gm_m3 / G

    # 平均半径 (km) → m
    radius_km = parse(r"[Vv]ol\.\s*[Mm]ean\s*[Rr]adius.*?=\s*([\d.]+)")
    radius_m  = radius_km * 1e3

    # 恒星自转周期 (d) → s
    t_days = parse(r"[Ss]idereal\s+rot\.?\s*period.*?=\s*([\d.]+)\s*d")
    t_s    = t_days * 86400.0

    # 自转轴北极方向 (RA, Dec) in ICRF 赤道系 (度)
    pole = re.search(
        r"[Pp]ole\s*\(RA,\s*Dec\).*?=\s*\(\s*([\d.]+)\s*,\s*([\d.]+)\s*\)",
        text, re.IGNORECASE
    )
    if not pole:
        raise ValueError("未能解析太阳自转轴方向（Pole RA, Dec）")
    ra_deg  = float(pole.group(1))
    dec_deg = float(pole.group(2))

    return {
        "mass_kg":    mass,
        "radius_m":   radius_m,
        "T_days":     t_days,
        "T_s":        t_s,
        "pole_ra_deg":  ra_deg,
        "pole_dec_deg": dec_deg,
        "gm_m3s2":    gm_m3,
    }


def sun_spin_angular_momentum(params: dict) -> np.ndarray:
    """
    计算太阳自转角动量向量（ICRF 赤道系）
      n̂  = 赤道坐标转 Cartesian（由北极 RA、Dec 给出）
      ω  = 2π / T
      I  = (2/5) · M · R²  （均匀实心球近似，定性分析用）
      L_☉ = I · ω · n̂
    """
    ra  = np.radians(params["pole_ra_deg"])
    dec = np.radians(params["pole_dec_deg"])
    n_hat = np.array([
        np.cos(dec) * np.cos(ra),
        np.cos(dec) * np.sin(ra),
        np.sin(dec),
    ])
    omega = 2.0 * np.pi / params["T_s"]
    I     = (2.0 / 5.0) * params["mass_kg"] * params["radius_m"] ** 2
    return I * omega * n_hat, n_hat, omega, I


# ══════════════════════════════════════════════════════════════════════
# 行星状态向量（ICRF 赤道系，以太阳为中心）
# ══════════════════════════════════════════════════════════════════════

def fetch_planet_vectors(planet_id: str):
    """
    从 Horizons 获取行星相对太阳的位置、速度向量。
    refplane='earth' → ICRF 赤道坐标系（与太阳北极 RA/Dec 同一参考系）
    返回：r (m)，v (m/s)
    """
    obj = Horizons(
        id=planet_id,
        location="@sun",
        epochs=EPOCH,
        id_type="majorbody",
    )
    vec = obj.vectors(refplane="earth")   # ← ICRF 赤道系

    r = np.array([float(vec["x"][0]),
                  float(vec["y"][0]),
                  float(vec["z"][0])]) * AU_TO_M

    v = np.array([float(vec["vx"][0]),
                  float(vec["vy"][0]),
                  float(vec["vz"][0])]) * AU_DAY_TO_MPS
    return r, v


# ══════════════════════════════════════════════════════════════════════
# 工具函数
# ══════════════════════════════════════════════════════════════════════

def mag(v: np.ndarray) -> float:
    return float(np.linalg.norm(v))

def fv(v: np.ndarray) -> str:
    return f"({v[0]:+.4e}, {v[1]:+.4e}, {v[2]:+.4e})"


# ══════════════════════════════════════════════════════════════════════
# 主程序
# ══════════════════════════════════════════════════════════════════════

def main():
    S1 = "═" * 84
    S2 = "─" * 84

    print(S1)
    print("  太阳系角动量计算（历元 2025-01-01，ICRF 赤道坐标系，SI 单位）")
    print("  参考系：以太阳质心为原点的 ICRF J2000.0 赤道惯性系")
    print("  数据源：NASA JPL Horizons System（全部在线拉取）")
    print(S1)

    # ── 1. 拉取太阳物理参数 ──────────────────────────────────────
    print("\n  正在从 JPL Horizons 获取太阳物理参数 ...", end="", flush=True)
    try:
        sun = fetch_sun_params()
        L_sun_vec, n_hat, omega, I_sun = sun_spin_angular_momentum(sun)
        print(" ✓")
    except Exception as e:
        print(f" ✗ 失败：{e}")
        sys.exit(1)

    print(f"\n  ☉  太阳物理参数（来自 JPL Horizons）")
    print(S2)
    print(f"  GM_☉      = {sun['gm_m3s2']:.6e}  m³/s²")
    print(f"  M_☉       = GM/G = {sun['mass_kg']:.6e}  kg")
    print(f"  R_☉       = {sun['radius_m']:.6e}  m  ({sun['radius_m']/1e3:.1f} km)")
    print(f"  T_☉       = {sun['T_days']:.4f} d  →  ω_☉ = {omega:.6e}  rad/s")
    print(f"  北极方向  RA={sun['pole_ra_deg']:.2f}°, Dec={sun['pole_dec_deg']:.2f}°  (ICRF)")
    print(f"  自转轴 n̂  = {fv(n_hat)}")
    print(f"  I_☉       = (2/5)·M·R²（均匀球近似）= {I_sun:.4e}  kg·m²")

    # ── 2. 拉取行星轨道角动量 ────────────────────────────────────
    print(f"\n{S1}")
    print("  正在查询各行星状态向量（ICRF 赤道系）...")
    print(S2)

    planet_L_sum = np.zeros(3)
    results = []

    for p in PLANETS:
        print(f"  {p['name']:<22} ...", end="", flush=True)
        try:
            r, v = fetch_planet_vectors(p["id"])
            L    = p["mass_kg"] * np.cross(r, v)
            planet_L_sum += L
            results.append({"name": p["name"], "r": r, "v": v, "L": L})
            print(" ✓")
        except Exception as e:
            print(f" ✗ {e}")

    # ── 3. 行星明细表 ────────────────────────────────────────────
    print(f"\n{S1}")
    print(f"  {'行星':<22} {'|r|(AU)':>9} {'|v|(km/s)':>10}  "
          f"{'L 向量 (kg·m²/s)':^50}  {'|L|(kg·m²/s)':>14}")
    print(S2)
    for res in results:
        r_au  = mag(res["r"]) / AU_TO_M
        v_kms = mag(res["v"]) / 1e3
        print(f"  {res['name']:<22} {r_au:>9.4f} {v_kms:>10.4f}  "
              f"{fv(res['L']):^50}  {mag(res['L']):>14.4e}")

    # ── 4. 汇总 ──────────────────────────────────────────────────
    grand_L = planet_L_sum + L_sun_vec
    pm = mag(planet_L_sum)
    sm = mag(L_sun_vec)
    gm_val = mag(grand_L)

    print(f"\n{S1}")
    print(f"  汇总：角动量矢量和（ICRF 赤道系，单位 kg·m²/s）")
    print(S2)

    print(f"  ① 行星轨道角动量矢量和  ΣL_planet")
    print(f"       向量 = {fv(planet_L_sum)}")
    print(f"       大小 = {pm:.6e}  kg·m²/s")

    print(f"\n  ② 太阳自转角动量  L_☉ = I_☉ · ω_☉ · n̂")
    print(f"       向量 = {fv(L_sun_vec)}")
    print(f"       大小 = {sm:.6e}  kg·m²/s")

    print(f"\n  ③ 全系统角动量矢量总和  L_total = ΣL_planet + L_☉")
    print(f"       向量 = {fv(grand_L)}")
    print(f"  ╔{'═'*62}╗")
    print(f"  ║   |L_total| = {gm_val:.6e}  kg·m²/s{' '*23}║")
    print(f"  ╚{'═'*62}╝")

    print(f"\n  占比分析：")
    print(f"    L_☉       / |L_total| = {sm/gm_val*100:6.2f}%")
    print(f"    ΣL_planet / |L_total| = {pm/gm_val*100:6.2f}%")
    jupiter = next((r for r in results if "Jupiter" in r["name"]), None)
    if jupiter:
        jm = mag(jupiter["L"])
        print(f"    L_木星    / |L_total| = {jm/gm_val*100:6.2f}%  （行星中贡献最大）")

    print(f"\n{S1}")
    print("  计算完成！")
    print(S1)


if __name__ == "__main__":
    main()

    