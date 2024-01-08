import tkinter as tk
import locale
import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer

###デフォルトモデルの指定(自分の環境に合わせ、各自書き換え)###
dir_txt = "TunedModel\misuzu-gpt2-medium"
tknz_txt = "rinna/japanese-gpt2-medium"

# モデルをセットアップする関数
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
    

# ウィンドウを作成する
def model_window():
    global entry1
    global entry2
    global lab3
    mdlwin = tk.Toplevel()
    mdlwin.title("モデル設定")
    mdlwin.geometry("300x200")  # ウィンドウのサイズを指定
    lab1 = tk.Label(mdlwin, text="model", font=("メイリオ", 10))
    lab1.grid(row=0, column=0)
    entry1 = tk.Entry(mdlwin, bg="white", fg="black", font=("メイリオ", 12))
    entry1.delete(0, tk.END)
    entry1.insert(tk.END,dir_txt)
    entry1.grid(row=0, column=1, columnspan=2)

    lab2 = tk.Label(mdlwin, text="tokenizer", font=("メイリオ", 10))
    lab2.grid(row=1, column=0)
    entry2 = tk.Entry(mdlwin, bg="white", fg="black", font=("メイリオ", 12))
    entry2.delete(0, tk.END)
    entry2.insert(tk.END,tknz_txt)
    entry2.grid(row=1, column=1, columnspan=2)

    
    lab3 = tk.Label(mdlwin, fg="red", font=("メイリオ", 10))
    lab3.grid(row=2, column=1)
    button1 = tk.Button(mdlwin, text="適用", font=("メイリオ", 10), command=apply_button_click)
    button1.grid(row=2, column=2, sticky=tk.E)  # ウィンドウにボタンを配置する

# ボタンの機能
def apply_button_click():
    global dir_txt
    global tknz_txt
    lab3.config(text="")
    try:
        dir_txt = entry1.get()
        tknz_txt = entry2.get()
        setup(dir_txt, tknz_txt)
    except Exception as e:
        # エラーが発生した場合の処理
        lab3.config(text="パスに誤りがあります")
