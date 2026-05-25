import numpy as np
import matplotlib.pyplot as plt

# 物理常数
k_B = 1.380649e-23       # 玻尔兹曼常数 (J/K)
T = 300                  # 温度 (K)
m = 28 * 1.66054e-27     # 分子质量,以 N2 为例 (kg)

# 特征速度尺度: v_c = sqrt(2 k_B T / m)
v_c = np.sqrt(2 * k_B * T / m)

# 横轴 v (m/s),取到 4 倍特征速度,保证曲线降到接近 0
v = np.linspace(0, 4 * v_c, 500)

# 目标函数: 只有指数部分,没有 v^2 前因子
f = np.exp(-m * v**2 / (2 * k_B * T))

plt.figure(figsize=(8, 5))
plt.plot(v, f, lw=2)
plt.xlabel(r'$v$  (m/s)')
plt.ylabel(r'$\exp\!\left(-\dfrac{mv^2}{2k_B T}\right)$')
plt.title(f'T = {T} K,  m = {m:.3e} kg')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()