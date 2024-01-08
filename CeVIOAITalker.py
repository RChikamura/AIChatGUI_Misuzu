# ライブラリの読み込み
import tkinter as tk
import win32com.client

# CeVIO AIの制御コンポーネントをディスパッチ
cevio = win32com.client.Dispatch("CeVIO.Talk.RemoteService2.ServiceControl2")

# CeVIO AIのトーク機能をディスパッチ
talker = win32com.client.Dispatch("CeVIO.Talk.RemoteService2.Talker2V40")

# 喋らせるキャラクターを設定
talker.Cast = "OИE";
talker.Volume = 100;
talker.Speed = 45;
talker.Tone = 67;
talker.Alpha = 35;
talker.ToneScale = 75;
talker.Components.At(0).Value = 50;
talker.Components.At(1).Value = 100;
talker.Components.At(2).Value = 0;
talker.Components.At(3).Value = 0;
talker.Components.At(4).Value = 0;

# しゃべらせる関数
def speech_speak(talk_word):
    # 喋らせたいテキストを指定
    state = talker.Speak(f"{talk_word}")

    # 喋りが終わるまで待機
    state.Wait()


# 設定ウィンドウを作成する
def cevio_window(target):
    global spkrlist
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    global entry6
    global entry7
    global entry8
    global entry9
    global entry10
    global lab8
    global lab9
    global lab10
    global lab11
    global lab12
    
    lab2 = tk.Label(target, text="話者", font=("メイリオ", 10))
    lab2.grid(row=0, column=1)
    
    # 話者リストボックスを配置する
    spkrlist = tk.Listbox(target, bg="white", fg="black", font=("メイリオ", 10))
    spkrlist.bind("<<ListboxSelect>>", select_cast)

    casts_obj = talker.AvailableCasts
    cast_array =  [casts_obj.At(i) for i in range(casts_obj.Length)]
    for cast in cast_array:
        spkrlist.insert(tk.END, f"{cast}")
    spkrlist.grid(row=1, column=1, rowspan=10)
           
    # 感情の名前取得
    emo_array =  ["None","None","None","None","None"]
    for i in range(5):
        if i < talker.Components.Length:
            emo_array[i] = talker.Components.At(i).Name 
        else:
            emo_array[i] ="None"

    # パラメータ設定
    lab3 = tk.Label(target, text="大きさ", font=("メイリオ", 10), width=6)
    lab3.grid(row=0, column=2)
    entry1 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry1.delete(0, tk.END)
    entry1.insert(tk.END, talker.Volume)
    entry1.grid(row=1, column=2)

    lab4 = tk.Label(target, text="速さ", font=("メイリオ", 10), width=6)
    lab4.grid(row=0, column=3)
    entry2 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry2.delete(0, tk.END)
    entry2.insert(tk.END, talker.Speed)
    entry2.grid(row=1, column=3)

    lab5 = tk.Label(target, text="高さ", font=("メイリオ", 10), width=6)
    lab5.grid(row=0, column=4)
    entry3 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry3.delete(0, tk.END)
    entry3.insert(tk.END, talker.Tone)
    entry3.grid(row=1, column=4)

    lab6 = tk.Label(target, text="声質", font=("メイリオ", 10), width=6)
    lab6.grid(row=0, column=5)
    entry4 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry4.delete(0, tk.END)
    entry4.insert(tk.END, talker.Alpha)
    entry4.grid(row=1, column=5)

    lab7 = tk.Label(target, text="抑揚", font=("メイリオ", 10), width=6)
    lab7.grid(row=0, column=6)
    entry5 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry5.delete(0, tk.END)
    entry5.insert(tk.END, talker.ToneScale)
    entry5.grid(row=1, column=6)
    
    lab8 = tk.Label(target, text=f"{emo_array[0]}", font=("メイリオ", 10), width=6)
    lab8.grid(row=2, column=2)
    entry6 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry6.delete(0, tk.END)
    entry6.insert(tk.END, talker.Components.At(0).Value)
    entry6.grid(row=3, column=2)
    
    lab9 = tk.Label(target, text=f"{emo_array[1]}", font=("メイリオ", 10), width=6)
    lab9.grid(row=2, column=3)
    entry7 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry7.delete(0, tk.END)
    entry7.insert(tk.END, talker.Components.At(1).Value)
    entry7.grid(row=3, column=3)

    lab10 = tk.Label(target, text=f"{emo_array[2]}", font=("メイリオ", 10), width=6)
    lab10.grid(row=2, column=4)
    entry8 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry8.delete(0, tk.END)
    entry8.insert(tk.END, talker.Components.At(2).Value)
    entry8.grid(row=3, column=4)

    #if talker.Components.Length > 3:
    lab11 = tk.Label(target, text=f"{emo_array[3]}", font=("メイリオ", 10), width=6)
    lab11.grid(row=2, column=5)
    entry9 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry9.delete(0, tk.END)
    entry9.insert(tk.END, talker.Components.At(3).Value)
    entry9.grid(row=3, column=5)

    #if talker.Components.Length > 4:
    lab12 = tk.Label(target, text=f"{emo_array[4]}", font=("メイリオ", 10), width=6)
    lab12.grid(row=2, column=6)
    entry10 = tk.Entry(target, font=("メイリオ", 10), width=6)
    entry10.delete(0, tk.END)
    entry10.insert(tk.END, talker.Components.At(4).Value)
    entry10.grid(row=3, column=6)
    

def cevio_remove():
    try:
        spkrlist.delete(0, tk.END)
    finally:
        print("CeVIO ")
    #widget.grid_remove()

def select_cast(event):
    talker.Cast = spkrlist.get(tk.ACTIVE);
    # 感情の名前取得
    emo_array =  ["None","None","None","None","None"]
    for i in range(5):
        if i < talker.Components.Length:
            emo_array[i] = talker.Components.At(i).Name 
        else:
            emo_array[i] ="None"


    lab8.config(text=f"{emo_array[0]}")
    lab9.config(text=f"{emo_array[1]}")
    lab10.config(text=f"{emo_array[2]}")
    lab11.config(text=f"{emo_array[3]}")
    lab12.config(text=f"{emo_array[4]}")

def cevio_apply():
    talker.Cast = spkrlist.get(tk.ACTIVE);
    talker.Volume = int(entry1.get());
    talker.Speed = int(entry2.get());
    talker.Tone = int(entry3.get());
    talker.Alpha = int(entry4.get());
    talker.ToneScale = int(entry5.get());
    talker.Components.At(0).Value = int(entry6.get());
    talker.Components.At(1).Value = int(entry7.get());
    talker.Components.At(2).Value = int(entry8.get());
    if talker.Components.Length > 3:
        talker.Components.At(3).Value = int(entry9.get());
    if talker.Components.Length > 4:
        talker.Components.At(4).Value = int(entry10.get());
    print("適用完了")
