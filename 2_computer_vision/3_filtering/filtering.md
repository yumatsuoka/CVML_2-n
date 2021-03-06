# 第3章 フィルタリング

フィルタリングによって画像から情報を取り出す方法に関する練習問題です．  
__キーワード: 輪郭抽出, ブラー, アンシャープマスク, ノイズ除去, 細線化__

- [2-3-1 エッジ検出](#edge)
- [2-3-2 ボケて](#blur)
- [2-3-3 ボケをなおして](#unsharp)
- [2-3-4 ノイズを載せて，除いて](#noise)
- [2-3-5 モルフォルジー](#morphology)
- [2-3-6 太文字](#thinning)

## <a name ="edge">2-3-1 エッジ検出
imageディレクトリにあるman.tifを変形し，以下の画像を作成せよ（保存形式は自由）．  
- 水平方向について3x3のSobelフィルタを適用したエッジ検出画像
- 垂直方向について3x3のSobelフィルタを適用したエッジ検出画像
- 水平方向および垂直方向の両方について3x3のSobelフィルタを適用したエッジ検出画像
- 水平方向および垂直方向の両方について3x3のPrewittフィルタを適用したエッジ検出画像

## <a name ="blur">2-3-2 ボケて
imageディレクトリにあるman.tifを変形し，以下の画像を作成せよ（保存形式は自由）．  
- 5x5の移動平均フィルタを適用したブラー画像
- 7x7の移動平均フィルタを適用したブラー画像
- 5x5のガウシアンフィルタを適用したブラー画像
- 7x7のガウシアンフィルタを適用したブラー画像

## <a name ="unsharp">2-3-3 ボケをなおして
[2-3-2 ボケて](#blur)で作成した「7x7のガウシアンフィルタを適用したブラー画像」に対して，アンシャープマスクをかけ，鮮鋭化画像を作成せよ（保存形式は自由）．  
適宜，マスクの係数値を変更して，係数値による鮮鋭化画像の変化を確認せよ．  

## <a name ="noise">2-3-4 ノイズを載せて，除いて
imageディレクトリにあるman.tifを変形し，以下の画像を作成せよ（保存形式は自由）．  
- ガウシアンノイズ (Gaussian noise) を付与したガウシアンノイズ画像
- ごま塩ノイズ (salt-pepper noise) を付与したごま塩ノイズ画像
- ガウシアンノイズ画像にメディアンフィルタを適用した画像
- ごま塩ノイズ画像にメディアンフィルタを適用した画像
- ごま塩ノイズ画像にバイラテラルフィルタを適用した画像

## <a name ="morphology">2-3-5 モルフォルジー
imageディレクトリにあるkanji.tifを変形し，以下の画像を作成せよ（保存形式は自由）．  
- クロージング処理 (3回膨張 + 1回収縮) を行なった画像
- オープニング処理 (3回収縮 + 1回膨張) を行なった画像

## <a name ="thinning">2-3-6 太文字
imageディレクトリにあるkanji.tifに対して細線化処理を行なった画像を作成せよ（保存形式は自由）．  
