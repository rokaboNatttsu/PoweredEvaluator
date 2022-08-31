式の文字列を入力し、文字があれば数値を代入し、近似値を計算する。微分積分や行列は扱えない。
シンプルな電卓とさほど変わらない機能。文字列を読んで計算するのが特徴。eval()の強化版として作った。

# 式の書き方のルール

計算順序を表す括弧はすべて()を使う。関数f(x)みたいな書き方はできないし、そもそも関数を定義する機能はない。

和：X+Y

差：X-Y

積：X*Y, *は省略不可

商(実数)：X/Y

商(何回割り切れるかのほう)：X//Y

余り：X%Y

XのY乗 : X**Y

ネイピア数のX乗：exp[X]

平方根：sqrt(X)

自然対数：log[X]

常用対数：log10[X]

底が2の対数：log2[X]

sin：sin[X]

cos：cos[X]


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

式の文字列から文字を抽出し、値のインプットを求めてくる。

### 辞書型のデータを使って代入

d = {
  "X":値,
  "Y":値,
  "Z":値,
}

evl.substitute(vdic=d)

### 近似値計算

計算結果 = evl.evaluate()

