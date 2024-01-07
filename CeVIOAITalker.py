# ライブラリの読み込み
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

# しゃべらせる関数
def speech_speak(talk_word):
    # 喋らせたいテキストを指定
    state = talker.Speak(f"{talk_word}")

    # 喋りが終わるまで待機
    state.Wait()
