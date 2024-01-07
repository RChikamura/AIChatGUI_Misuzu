# AIChatGUI

このプログラムは、ローカル動作の自然言語処理AIを使って、文章を送ると返答をもらうことができるPythonプログラムです。

OpenAI社などが提供する、自然言語処理AIのAPIには対応しておりません。

## 主な機能

* 入力文に対し、AIから返信をもらう
* 返信の読み上げ(現在はCeVIO AI OИE(近村美鈴カスタム)のみ対応)

## 使い方

※この方法でAIをセットアップした場合、返答は生成されますが、文脈や前の内容を受けての返答はできません。

### 1. AIのファインチューニングデータを用意

入力文(呼びかけ)と出力文(応答)をまとまった数用意し、以下の形式にしてください

```<s>入力文(呼びかけ)[SEP]出力文(応答)</s><s>...```

使用するデータを用意できない場合、[つくよみちゃん会話AI計画](https://tyc.rei-yumesaki.net/material/kaiwa-ai/)のデータを書き換えるのがおすすめです

(そのまま使うと癖の強いキャラになる可能性が高い)

### 2. 使用するAIのファインチューニング

使用するAIに合わせ、ファインチューニングを実行してください

これは、AIをキャラになりきらせるためだけでなく、出力形式をプログラムの想定する形にするためにも必要なので、必ず行ってください。

ファインチューニングができたら、生成されたファイルをダウンロードし、空のフォルダに入れておいてください

### 3. プログラムのダウンロード

コマンドプロンプトを起動し、プログラムをインストールしたいディレクトリで

```git clone https://github.com/RChikamura/AIChatGUI_Misuzu.git```

を実行してください。

コマンドに抵抗がある方は、コードページ(ファイル一覧みたいなのがあるところ)で、ファイル一覧の右上にある、緑色の```<>Code```ボタンをクリックし、```Download ZIP```をクリックして、zipファイルを入手してください。
![zipファイルのダウンロード](https://github.com/RChikamura/AIChatGUI_Misuzu/assets/76420242/e434b1e4-0658-4f66-948b-b33a85c587f4)

### 4. ライブラリのインストール

付属の setup.bat を実行してください。

### 5. モデル情報の書き換え

テキストエディタでRunChatGUI.pyを開き、以下の２つを書き換えてください。

```dir_txt```(13行目)　ダウンロードしたファインチューニング済みモデルが入っているフォルダのパス

```tknz_txt```(14行目)　使用するトークナイザー(自然言語をAIが理解できる形に変換する)の指定。基本的には、ファインチューニングに使ったモデルと同じでよい

### 6. プログラムの起動と動作

コマンドプロンプトを起動し、プログラムをインストールしたいディレクトリで

```python RunChatGUI.py```

を実行してください。しばらくすると、プログラムが起動し、以下のような画面が表示されます。

![アプリケーションの画面](https://github.com/RChikamura/AIChatGUI_Misuzu/assets/76420242/9a8ebb95-e210-4a46-a699-1f149a2a6f5e)

テキストボックスに文章を入力し、送信ボタンをクリックすると、返答が生成され、表示されます。この時、CeVIO AIで音声合成 にチェックが入っていれば、音声も合成されます。

(CeVIO AI OИEがインストールされており、CeVIO AIアプリケーションが起動している場合のみ。それ以外はたぶんエラーになる)

再生ボタンを押すと、最新の返答がもう一度読み上げられます。

## 必要な環境

おそらく、以下の環境があれば動作します

(作者は素人であり、検証できる環境もないので、保証はできません。)
 
* Python 3.10.1
* torch 2.1.2
* protobuf 3.20.1 (最新版は互換性がないため注意)
* transformers 4.36.2
* sentencepiece 0.1.99
* pywin32 306 (CeVIO AIとCOM連携するために必要)

Windowsであれば、setup.batを実行すれば必要なライブラリは大体インストールされるはずです。

作者の環境にインストールされているライブラリはenvironment.txtに記載されているので、動かなかった場合、参考にしてください。

## 今後の開発予定

* 使用モデルやトークナイザー、音声の設定をGUIでできるようにしたい
* YouTubeのAPIと連携可能にし、チャットに応答できるようにしたい

## その他

私が使用しているモデルが、「こんにちは！」に対し、「です。～」と返すため、文頭が「です」だった場合、「こんにちは」に置換されるようにしています。

## 参考文献

AIのファインチューニングは、以下のサイトを参考にしております

https://qiita.com/Yokohide/items/e74254f334e1335cd502
