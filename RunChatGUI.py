# ライブラリの読み込み
import tkinter as tk
import locale
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import ModelSetting as mconf # モデル設定関連
import VoiceSetting as vconf # 音声設定関連
import CeVIOAITalker as cevio #CeVIO AI関連のファイル

# 文字コードの設定(念のため)
locale.getpreferredencoding = lambda: "UTF-8"

###UI関連###
# ウィンドウを作成する
window = tk.Tk()
window.title("AIチャットアプリ")
window.geometry("600x400")  # ウィンドウのサイズを指定

# メニューバーの作成
menubar = tk.Menu(window)
window.config(menu=menubar)

# メニュー関連の関数

# メニュー項目の追加
file_menu = tk.Menu(menubar, tearoff=0)
#file_menu.add_command(label="ファイルを開く")
#file_menu.add_command(label="ファイルを保存")
#file_menu.add_separator()
file_menu.add_command(label="終了", command=window.quit)

setting_menu = tk.Menu(menubar, tearoff=0)
setting_menu.add_command(label="モデル設定", command=lambda:mconf.model_window())
setting_menu.add_command(label="音声合成の設定", command=lambda:vconf.voice_window())

# メニューバーに項目を追加
menubar.add_cascade(label="ファイル", menu=file_menu)
menubar.add_cascade(label="設定", menu=setting_menu)

# メッセージを定義する(関数で使用するため、あらかじめ定義)
sent = "こんにちは！"
message = tk.Message(window, text=f"{sent}", font=("メイリオ", 12), width=450)

# UIの配置
lab1 = tk.Label(window, text="テキスト", font=("メイリオ", 10))
lab1.grid(row=0, column=0)
entry = tk.Entry(window, bg="white", fg="black", font=("メイリオ", 12), width=48)
entry.grid(row=0, column=1)
button1 = tk.Button(window, text="送信！", font=("メイリオ", 10), command=lambda:generate_reply(entry.get()))
button1.grid(row=0, column=2)

lab2 = tk.Label(window, text="返答", font=("メイリオ", 10))
lab2.grid(row=1, column=0)

button2 = tk.Button(window, text="再生", font=("メイリオ", 10), command=lambda:cevio.speech_speak(sent))
button2.grid(row=1, column=2)

message.grid(row=1, column=1)

checkbox_var = tk.IntVar()

checkbox = tk.Checkbutton(window, text="CeVIO AIで音声合成", variable=checkbox_var)
checkbox_var.set(False)
checkbox.grid(row=2, column=1)

###AI関連###
# テキスト生成の準備
mconf.setup(mconf.dir_txt, mconf.tknz_txt)

# 返事を生成する関数
def generate_reply(inp, num_gen=1):
    global sent
    input_text = "<s>" + str(inp) + "[SEP]"
    input_ids = mconf.tokenizer.encode(input_text, return_tensors='pt').to(mconf.device)
    flag = True
    error_count = 0

    while flag == True:
        out = mconf.model.generate(input_ids, do_sample=True, max_length=64, num_return_sequences=num_gen,
                            top_p=0.95, top_k=20, bad_words_ids=[[1], [5]], no_repeat_ngram_size=3)
        for sent in mconf.tokenizer.batch_decode(out):
            sent = sent.split('[SEP]</s>')[1]
            sent = sent.replace('</s>', '')
            sent = sent.replace('<br>', '\n')
            if not sent.startswith('_') and not sent.startswith('<') and not sent.startswith('は、') and error_count < 5:
                if sent.startswith('です'):
                    sent = sent.replace('です', 'こんにちは', 1)
                message.config(text=f"{sent}")
                flag = False
                if checkbox_var.get():
                    cevio.speech_speak(sent)
            else:
                error_count += 1
                print("Failed to generate " + str(error_count) + " times. Retrying...")

# ウィンドウを表示する
window.mainloop()
