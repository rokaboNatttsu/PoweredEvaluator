式の文字列を入力し、文字があれば数値を代入し、近似値を計算する。微分積分や行列は扱えない。
計算できることは、シンプルな電卓とさほど変わらない機能。文字列を読んで計算するのが特徴。eval()の強化版として作った。
文字を使った式を定義したり、タイミングをずらして代入したりするために作った。

引数が2つの関数も適応できるように変更するかもしれない。comb,
必要に迫られたら。



# 使い方

基本的に、電卓のような使い方になる。

### 計算する式の定義

eq="式の文字列"

evl = PoweredEvaluator(eq)

### 式の文字列の取得

evl.eq

### まとめて代入

evl.direct_substitute(X=値, Y=値,..., Z=値)

evl.direct_substitute("X"=値, "Y"=値,..., "Z"=値)
ではない。

### 対話的代入

evl.interactive_substitute()

input value of x : 

式の文字列から文字を抽出し、値のインプットを求めてくる。代入していないすべての変数に代入する。

### 辞書型のデータを使って代入

d = {
  "X":値,
  "Y":値,
  "Z":値,
}

evl.substitute(vdic=d)

### 近似値計算

計算結果 = evl.evaluate()




# 式の書き方

### ルール

計算順序を表す括弧はすべて()を使う。関数f(x)みたいな書き方はできないし、そもそも関数を定義する機能はない。

和：X+Y

差：X-Y

積：X*Y, *は省略不可

商(実数)：X/Y

商(何回割り切れるかのほう)：X//Y

余り：X%Y

XのY乗 : X**Y


関数は、引数を[]中に書く。例えば、

exp[X], sqrt[X], log[X], sin[X]



### 関数
xの絶対値：abs[x]

ネイピア数のx乗：exp[x]

xの自然対数：log[x]

xの常用対数：log10[x]

底が2の対数：log2[x]

平方根：sqrt[x]

e^x - 1：expm1[x]

ln(1+x)：log1p[x]

sin, cos, tan：sin[x], cos[x], tan[x]

cosh, sinh, tanh：cosh[x], sinh[x], tanh[x]

arctan, arcsin, arccos：atan[x], asin[x], acos[x]

arccosh, arcsinh, arctanh：acosh[x], asinh[x], atanh[x]

erf, erfc：erf[x], erfc[x]



### 定数と無限大
普通の変数名に使っちゃダメな奴

π：pi

e：e

無限大：inf
