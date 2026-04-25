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
> 現代的な惑星形成の研究は，系外惑星の発見以前，20世紀後半から太陽系
> 形成の研究として始まった．ここでは説明すべき太陽系の主な特徴について
> まとめておこう．図2.1に太陽系の天体の分類を示す．
>
> まず，惑星系全体としての特徴を見てみよう．惑星の総質量は太陽質量の
> 約$1/1000$倍しかなく，そのほとんどは木星と土星に集中している．一方，惑
> 星の軌道角運動量の大きさは太陽の自転角運動量の約190倍にもなる．つま
> り，太陽系では質量は太陽に集中し，角運動量は惑星に集中している．

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

m = m_{sun} + m_{planets} 
= 1 + 1e-3 [太陽質量], 

$r = 10^7 + 4.5e9$ [kg]
以上のことにより，太陽系では角運動量が惑星に集中している

---

>太陽系には内側から外側へ向かって,地球型(岩石),木星型(ガス),海
>王星型(氷)の組成の異なる3種類の惑星が並んでいる.水星,金星,地球,
>火星は地球型惑星で,岩石質の惑星である.木星と土星はガスを主成分とす
>る木星型惑星で,ガスの主成分は水素とヘリウムである.天王星と海王星は
>海王星型惑星で,ガス成分は質量の約10\%しかなく,質量のほとんどは氷
>(水,メタン,アンモニアを主成分とする混合物)である.これらの惑星の平
>均密度は,組成を反映して,地球型は$3.9\text{--}5.5\,\mathrm{g\,cm^{-3}}$,木星型と海王星型は
>$\simeq 1.0\,\mathrm{g\,cm^{-3}}$になっている.また,軌道範囲と組成だけでなく,質量範囲も
>異なっていて,地球型は$\sim 0.1\text{--}1\,M_\oplus$,木星型は$\sim 100\,M_\oplus$,海王星型は
>$\sim 10\,M_\oplus$となっている.惑星の内部構造は基本的に密度成層を成しており,
>地球型では鉄の核の周りに岩石,木星・海王星型では主に岩石・氷等の重元
>素からなる固体核の周りに流体であるガスや氷となっている.最近の惑星探
>査によって,木星や土星の固体核と流体部分ははっきりと層で区別されてい
>るのではなく混合されていて,密度変化は連続的になっていることが明らか
>になってきている.

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
>天体の外側は彗星の巣であるオールトの雲に接続し,その外縁は太陽の潮汐半径($\simeq 2\times 10^5\,\mathrm{au}$)になっている.彗星とは氷小天体が揮発性大気をもつ状態を指す.


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

#### 円盤不安定モデル

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