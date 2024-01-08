import tkinter as tk
import locale
import CeVIOAITalker as cevio #CeVIO AI関連のファイル

# 設定ウィンドウを作成する
def voice_window():
    global vcwin
    global list1
    vcwin = tk.Toplevel()
    vcwin.title("音声設定")
    vcwin.geometry("600x400")  # ウィンドウのサイズを指定
    
    lab1 = tk.Label(vcwin, text="ソフト選択", font=("メイリオ", 10))
    lab1.grid(row=0, column=0)
    
    list1 = tk.Listbox(vcwin, bg="white", fg="black", font=("メイリオ", 10)) 
    list1.bind("<<ListboxSelect>>", select_soft)
    list1.insert(tk.END, "CeVIO AI")
    #list1.insert(tk.END, "VOICEVOX")
    list1.grid(row=1, column=0, rowspan=10)
    
      
    # ボタンを配置する
    button1 = tk.Button(vcwin, text="適用", font=("メイリオ", 10))
    button1.grid(row=11, column=6, sticky=tk.E)  # ウィンドウにボタンを配置する
    
def select_soft(event):
    #try:
        #cevio.cevio_remove()
    #finally:
        #print("UI初期化")
    global soft
    soft = list1.get(tk.ACTIVE)
    if soft == "CeVIO AI": 
        cevio.cevio_window(vcwin)
        
def apply_soft():
    if soft == "CeVIO AI": 
        cevio.cevio_apply()
