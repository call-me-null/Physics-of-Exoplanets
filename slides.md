---
theme: default
colorSchema: light
background: white
class: bg-white text-black
drawings:
  persist: false
transition: slide-left
comark: true
---

<style>
.slidev-layout {
  background: white !important;
  color: black !important;
}

/* academic cover style */
.cover-title {
  font-family: "Times New Roman", Georgia, serif;
  font-size: 2.6rem;
  font-weight: 600;
  text-align: center;
  letter-spacing: 0.01em;
  line-height: 1.2;
  margin-top: 4rem;
  margin-bottom: 1rem;
  color: #111;
  white-space: nowrap;
}

.cover-subtitle {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1.2rem;
  font-weight: 400;
  text-align: center;
  letter-spacing: 0.08em;
  color: #444;
  margin-bottom: 2.5rem;
}

.cover-line {
  width: 180px;
  height: 1px;
  background: #888;
  margin: 0 auto 2rem auto;
}
</style>

<div class="cover-title">
  系外惑星の物理
</div>

<div class="cover-line"></div>

<div class="cover-subtitle">
  
</div>

---

## 惑星形成の考え方
>惑星系は恒星形成の副産物として形成されるガスとダスト(固体微粒子)
>からなる星周円盤(原始惑星系円盤)から形成される.形成の時間スケール
>は$\sim 1\text{--}10$億年,空間スケールは惑星系なら$\sim 10\,\mathrm{au}$,彗星雲まで含めると
>$\sim 10^5\,\mathrm{au}$にもなる.そして,円盤内でサブミクロンサイズのダストは
>$1000\text{--}100000\,\mathrm{km}$サイズの惑星へと成長していく.この惑星形成の過程は,
>現代的な惑星形成論の創始者の一人である林忠四郎によれば,次のような物理過程
>ということができる.
> - 巨大な原子集団の長期かつ複雑多岐にわたる非可逆過程
> - 原子・分子・光子の相互作用に関する微視的法則と重力が主役である巨視的な運動法則の両者によって規定

>このようにミクロからマクロまでの物理が複雑に関連し合っている物理過
>程を調べることは一筋縄でいかない部分もあるが,その分,豊かで面白い系
>ということもできる.このような性質をもつ物理過程である惑星形成を理解
>するには,要素還元的なアプローチが適している.すなわち
> - 形成過程を本質的な素過程に還元し物理を理解する.
> - 素過程を総合して形成理論を構築する.
>という方法である.

恒星形成とは

サブミクロン：亚微米

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>


---

### 太陽系の特徴
> 現代的な惑星形成の研究は，系外惑星の発見以前，20世紀後半から太陽系形成の研究として始まった．
>ここでは説明すべき太陽系の主な特徴についてまとめておこう．図2.1に太陽系の天体の分類を示す．
>
> まず，惑星系全体としての特徴を見てみよう．惑星の総質量は太陽質量の約$1/1000$倍しかなく，そのほとんどは木星と土星に集中している．
>一方，惑星の軌道角運動量の大きさは太陽の自転角運動量の約190倍にもなる．つまり，太陽系では質量は太陽に集中し，角運動量は惑星に集中している．

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>

角運動量
$\boldsymbol{L}
= \boldsymbol{r} \times \boldsymbol{p}
= m \boldsymbol{r} \times \boldsymbol{v}$

数値的に $L = rp\sin\theta = mrv\sin\theta$

$m_{\odot} ~ 1, m_{planets} ~ 10^{-3}$

ICRFにおいて，太陽が均一な球体と見なす

$L_{planets} = 3.134815 \cdot 10^{43}  kg·m²/s (99.39\%total)$

$L_{\odot} = 1.930377 \cdot 10^{41} kg·m²/s (0.61\%total)$

$L_{Jupiter} / L_{total} = 61.12\%$

$L/m = \sqrt{G m_{\cdot}a(1-e^2)}$

---

>太陽系には内側から外側へ向かって,地球型(岩石),木星型(ガス),海王星型(氷)の組成の異なる3種類の惑星が並んでいる.
>水星,金星,地球,火星は地球型惑星で,岩石質の惑星である.
>木星と土星はガスを主成分とする木星型惑星で,ガスの主成分は水素とヘリウムである.
>天王星と海王星は海王星型惑星で,ガス成分は質量の約10\%しかなく,質量のほとんどは氷(水,メタン,アンモニアを主成分とする混合物)である.
>これらの惑星の平均密度は,組成を反映して,地球型は$3.9\text{--}5.5\,\mathrm{g\,cm^{-3}}$, 木星型と海王星型は $\simeq 1.0\,\mathrm{g\,cm^{-3}}$になっている.
>また,軌道範囲と組成だけでなく,質量範囲も異なっていて,地球型は$\sim 0.1\text{--}1\,M_\oplus$,木星型は$\sim 100\,M_\oplus$,海王星型は$\sim 10\,M_\oplus$となっている.
>惑星の内部構造は基本的に密度成層を成しており,地球型では鉄の核の周りに岩石,木星・海王星型では主に岩石・氷等の重元素からなる固体核の周りに流体であるガスや氷となっている.
>**最近の惑星探査によって,木星や土星の固体核と流体部分ははっきりと層で区別されているのではなく混合されていて,密度変化は連続的になっていることが明らかsになってきている.**

地球密度　5.52　岩石　2.9-3.5

**木星の密度の調べ方**

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>


---


>惑星の軌道には共通の特徴がある.軌道はほぼ円軌道で,軌道離心率は
>$e \lesssim 0.1$になっている.また,軌道面は揃っていて,惑星の平均軌道面(不変
>面)に対しての軌道傾斜角(ラジアン)は$I \lesssim 0.1$となっている.つまり,惑
>星の軌道は同一平面内の太陽を中心とする同心円になっている.そしてすべ
>ての惑星は軌道上を同じ方向に公転運動している.
>
>惑星の自転は,金星と天王星を除くと,順行(軌道運動と同方向)であり,
>自転軸傾斜角は$\varepsilon \lesssim 0.5$である.金星は逆行しており$\varepsilon \simeq \pi$,天王星は
>$\varepsilon \simeq \pi/2$となっている.自転周期は,水星は59日,金星は243日であるが,他は
>半日から1日となっている.
>
>太陽系には惑星以外にも太陽系小天体と呼ばれる小天体が無数に存在して
>いる.これらは軌道範囲で分類されていて,木星軌道以内を小惑星,海王星
>軌道以遠を太陽系外縁天体と呼ぶ.その間にはケンタウルス天体と呼ばれる
>小惑星と太陽系外縁天体の間の遷移的な小天体が存在している.太陽系外縁
>天体の外側は彗星の巣であるオールトの雲に接続し,その外縁は太陽の潮汐半径($\simeq 2\times 10^5\,\mathrm{au}$)になっている.**彗星とは氷小天体が揮発性大気をもつ状態を指す.**

水星公転周期８８日，金星


<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>

---

### 太陽系の形成モデル

>太陽系形成論は未だ発展途上で,現在も様々なモデルが提唱されている.
>ここではまず,現在でも基礎となっている古典的な太陽系形成モデルの概要について紹介しよう.
>
>太陽系形成モデルには,大きく分けて円盤不安定モデルと核集積モデルの2つの考え方がある.
>円盤不安定モデルは提唱者の名前からキャメ
>ロンモデル,核集積モデルは研究が行われた大学の所在地から京都モデルとも呼ばれる.
>表2.1に,2つのモデルの特徴をまとめる.

<table class="formation-table">
  <caption>表 2.1 太陽系形成モデル</caption>
  <thead>
    <tr>
      <th>モデル</th>
      <th>
        <div class="th-center">
          円盤質量 <span class="math">M<sub>☉</sub></span>
        </div>
      </th>
      <th>基本材料</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>円盤不安定</td>
      <td><span class="math">≃ 1</span></td>
      <td>原始ガス惑星</td>
    </tr>
    <tr>
      <td>核集積</td>
      <td><span class="math">≃ 0.01</span></td>
      <td>微惑星</td>
    </tr>
  </tbody>
</table>

<style>
.formation-table {
  width: auto;
  min-width: 28em;
  max-width: 70%;
  margin: 0.6em auto;
  border-collapse: collapse;
  font-size: 0.75em;
  line-height: 1.35;
}

.formation-table caption {
  caption-side: top;
  margin-bottom: 0.35em;
  font-size: 0.9em;
  font-weight: bold;
  text-align: center;
}

.formation-table th,
.formation-table td {
  border: 1px solid currentColor;
  padding: 0.25em 0.65em;
  text-align: center;
  vertical-align: middle;
  white-space: nowrap;
}

.formation-table .th-center {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.2em;
}

.formation-table .math {
  font-family: KaTeX_Main, "Times New Roman", serif;
}
</style>

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>

---

#### 円盤不安定モデル Disk instability 

>円盤不安定モデルの特徴は,$\simeq 1\,M_\odot$と大きな質量の原始惑星系円盤を仮定することと,
>惑星のマクロな基本材料(ビルディングブロック)として原始ガス惑星を考えることにある.
>このモデルでは原始惑星系円盤の重力不安定性によって円盤から直接惑星が形成される.
>基本シナリオは以下の通りである.
> 1. 重力不安定による円盤の分裂で原始ガス惑星が形成される.
> 2. 原始ガス惑星中で固体成分が中心に沈殿し固体核が形成される.
> 3. ガスを失うことで固体惑星が形成される.
<blockquote>
  <p>
    このモデルには重力不安定性という軌道周期程度の短い時間スケールで原
    始ガス惑星を形成できるという長所がある.一方,ガス惑星のガスを散逸さ
    せることで,岩石・氷惑星を形成させるわけだが,巨大で重力の強い惑星か
    らガスを散逸させるのは容易ではない.また,小惑星,太陽系外縁天体,彗
    星のような固体小天体をどのように形成するのかも問題だ.そもそも,重力
    的に不安定な原始惑星系円盤が形成されるかという問題もある.以上のこと
    から,現在は円盤不安定モデルは太陽系形成には適さないと考えられている.
    しかし,近接ガス惑星や大離心率惑星などの系外惑星の形成では円盤不安定
    モデルが有効な可能性があり,再び脚光を浴びている.
  </p>
</blockquote>

Disk instability 

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>

---

#### 核集積モデル

>核集積モデルは,$\simeq 0.01\,M_\odot$と小さい質量の原始惑星系円盤を考え,さらに固体小天体,微惑星という基本材料を仮定する.
>この微惑星仮説に基づく形成シナリオは以下の通りである.
> 1. ダストの集積によって微惑星が形成される.
> 2. 微惑星の集積によって固体惑星が形成される.
> 3. 固体惑星がガスを捕獲することによってガス惑星が形成される.
>
>微惑星仮説は地球型惑星と海王星型惑星はもちろんのこと,木星型惑星でも重元素存在比が太陽組成より大きいことを説明できる.
>また,固体小天体の存在とも調和的である.この考え方は,ガス惑星の形成過程,すなわち最初に固体核(惑星)が形成されてそれがガスを捕獲する,から核集積モデルと呼ばれる.
>
>現在,核集積モデルは太陽系形成だけでなく,系外惑星形成でも標準シナリオになっている.以下では核集積モデルをさらに詳しく説明する.

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>

ガス・埃　ーー＞　固体核　ーー＞　微惑星　ーー＞　惑星

現在の主要モデル

---

>核集積モデルでは,原始惑星系円盤からの惑星形成は,
>1. ダストからの微惑星の形成,
>2. 微惑星からの原始惑星の形成,
>3. 原始惑星からの惑星の形成,
>の3段階からなる.
>
>(1)は最も解明されていない段階で,微惑星形成について様々なモデルが提案されているが,未だに決定打がない状況だ.
>微惑星は古典的なモデルでは$\sim 1\,\mathrm{km}$サイズの固体天体で,これはダスト層の重力不安定によって形成されるサイズになっている.
>(2)はコンピュータシミュレーションによって比較的よく研究されていて,標準的な惑星集積のモデルが確立されている.
>原始惑星とは一部の成長した大型微惑星のことである.(1)と(2)は惑星形成に共通の段階だが,(3)は惑星の種類ごとに過程が異なる.
>地球型惑星は原始惑星の衝突合体によって形成され,
>原始惑星(固体核)が原始惑星系円盤からガスを捕獲することによって木星型惑星と海王星型惑星は形成されると考えられている.

1. ダスト　ーー＞　微惑星　：解明済
2. 微惑星　ーー＞　原始惑星：シミュで研究
3. 原始惑星　ーー＞　惑星：岩石惑星（衝突），ガスと氷惑星（捕獲）
疑問点：微惑星段階に抵抗増加による太陽へ落ちる可能性

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>

---

> #### 基本運動と相互作用
>系の基本運動について考えよう.支配的な力は中心星重力なので,基本運動は粒子もガスも中心星周りの公転運動になる.よって,
>系の力学的時間スケールは公転周期になる.そして,中心星重力以外の力が摂動として働き,
>公転運動の軌道が変化していく.摂動としては,粒子間相互作用,ガスの粘性拡散,粒子ガス間相互作用,電磁相互作用等が考えられる.
>摂動の時間スケールは一般に力学的時間スケールよりも非常に長く,形成過程の時間スケールを決めることになる.
>
>粒子間相互作用としては,粒子の重力相互作用と物理的衝突がある.
>また,粒子ガス間相互作用としては,流体力学的抵抗,重力的抵抗,降着等がある.
>さらに,粒子が帯電していたり,ガスがイオン化したりしていれば,磁場との相互作用がある.粒子とガスともに光子や宇宙線とも相互作用する.

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>


---

>#### 軌道・集積・組成進化
>ダストとガスから惑星への形成過程には,物質の軌道・集積・組成進化の3つの軸がある.これらはお互いに影響し合いながら全体として進んでいく.
>
>軌道進化は,上述した通りで,相互作用による摂動によってエネルギーや角運動量が変化するために起きる.軌道の変化は最終的に物質の空間的配置を決める.
>
>集積進化は物質の質量またはサイズの変化である.これは粒子間衝突による合体・破壊によって引き起こされる.
>また,天体の重力によるガス降着も集積進化である.
>一般に軌道進化によって集積進化が規定されていて,軌道進化の時間スケールよりも集積の時間スケールの方が長い.
>
>最後に組成進化である.これは集積進化とともに進行し,衝突脱ガス,分化や化学反応による物質の化学変化を表す.

<style>
blockquote {
  padding: 0.5em 1em;
  border-left: 4px solid currentColor;
  line-height: 1;
}

blockquote p {
  text-indent: 1em;
  margin: 0 0 0.8em;
  line-height: 1.2;
}

blockquote p:last-child {
  margin-bottom: 0;
}
</style>

---

>#### 研究手法
>惑星形成の力学的な基本問題は,粒子の分布関数$f(m, \bm{x}, \bm{v})$の進化を調べることである.
>惑星系は回転系なので,位相空間$(\bm{x}, \bm{v})$の代わりに,軌道要素$(a, e, I, \Omega, \omega, t_0)$を使うことが多い.
>特にエネルギーと角運動量に関係する$(a, e, I)$は重要である.$f(m, a, e, I)$の進化は以下で見るように複雑で非線形な過程なので,
>解析的に進化を記述するのは難しい.そこでコンピュータを使ったシミュレーションによる研究が行われている.
>粒子の軌道・集積進化について現在用いられている3つの研究方法とその特徴を簡単に紹介しよう.


---

> **統計的手法** $f$の進化をオイラー的に解く方法.粒子の凝集(スモルコフスキー)方程式を解くことで質量分布の進化を追う.
>計算は比較的軽く大粒子数を扱うことが可能である(現状では最大で$\sim 10^9$粒子).自由空間近似を基礎としているため空間構造の進化は解くのは難しい.
>主として惑星集積前期の研究に用いられる.
>
>**$N$体シミュレーション** $f$の進化をラグランジュ的に解く方法.粒子の運動方程式を解くことで軌道進化や衝突を調べる.
>計算量が膨大なため使える粒子数は限られる(現状では最大で$\sim 10^6$粒子).空間構造の進化を自然に計算できる.主として惑星集積後期の研究に用いられる.
>
>**惑星分布生成モデル** 形成の素過程の解析解や経験式を用いて$f$の進化を記述する.
>初期条件や進化過程に確率的扱いを導入し,多数の計算を行うことで惑星分布を生成する.
>現状では微惑星以降惑星系まで扱うことができ,系外惑星の観測と比較される.

統計的：ダストの集積；N体積分：衝突を研究；モデル：系外惑星に使用

---

## 原始惑星系円盤の標準モデル
太陽系の形成に基づくモデル，
### 温度分布
**雪線**
