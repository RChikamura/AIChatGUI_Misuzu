# ライブラリの読み込み
import tkinter as tk
import locale
import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer
import CeVIOAITalker as cevio #CeVIO AI関連のファイル

# 文字コードの設定(念のため)
locale.getpreferredencoding = lambda: "UTF-8"

###モデルの指定(自分の環境に合わせ、各自書き換え)###
dir_txt = "TunedModel\misuzu-gpt2-medium"
tknz_txt = "rinna/japanese-gpt2-medium"

###UI関連###
# ウィンドウを作成する
window = tk.Tk()
window.title("AIチャットアプリ")
window.geometry("600x400")  # ウィンドウのサイズを指定

# メニューバーの作成
menubar = tk.Menu(window)
window.config(menu=menubar)

# メニュー項目の追加
file_menu = tk.Menu(menubar, tearoff=0)
#file_menu.add_command(label="ファイルを開く")
#file_menu.add_command(label="ファイルを保存")
#file_menu.add_separator()
file_menu.add_command(label="終了", command=window.quit)

setting_menu = tk.Menu(menubar, tearoff=0)
setting_menu.add_command(label="モデル設定")
setting_menu.add_command(label="音声合成の設定")

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

button2 = tk.Button(window, text="再生", font=("メイリオ", 10), command=lambda:speech_speak(sent))
button2.grid(row=1, column=2)

message.grid(row=1, column=1)

#def on_enter_pressed(event):
    #dir_txt = modeldir.get()
    #output = Path(f"{dir_txt}")
    #label.config(text=f"{dir_txt}")

#modeldir = tk.Entry(window, bg="lightgray", fg="black", font=("Arial", 12))
#modeldir.delete(0, tk.END)
#modeldir.insert(tk.END, dir_txt)
#modeldir.bind("<Return>", on_enter_pressed)
#modeldir.grid(row=2, column=1)
checkbox_var = tk.IntVar()

checkbox = tk.Checkbutton(window, text="CeVIO AIで音声合成", variable=checkbox_var)
checkbox_var.set(True)
checkbox.grid(row=2, column=1)

###AI関連###
# テキスト生成の準備
def setup(mdl_dir, tknz):
    output = Path(f"{mdl_dir}")
    global device
    global tokenizer
    global model

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer = AutoTokenizer.from_pretrained(f"{tknz}")
    tokenizer.do_lower_case = True
    model = AutoModelForCausalLM.from_pretrained(output)
    model.to(device)
    model.eval()
    
setup(dir_txt, tknz_txt)

# 返事を生成する関数
def generate_reply(inp, num_gen=1):
    global sent
    input_text = "<s>" + str(inp) + "[SEP]"
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    flag = True
    error_count = 0

    while flag == True:
        out = model.generate(input_ids, do_sample=True, max_length=64, num_return_sequences=num_gen,
                            top_p=0.95, top_k=20, bad_words_ids=[[1], [5]], no_repeat_ngram_size=3)
        for sent in tokenizer.batch_decode(out):
            sent = sent.split('[SEP]</s>')[1]
            sent = sent.replace('</s>', '')
            sent = sent.replace('<br>', '\n')
            if not sent.startswith('_') and not sent.startswith('<') and error_count < 5:
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
