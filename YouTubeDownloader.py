# https://ithelp.ithome.com.tw/users/20140047/ironman/4481
# https://vocus.cc/article/624e6738fd89780001ae7c1e
# https://ithelp.ithome.com.tw/articles/10278264
# https://www.delftstack.com/zh-tw/tutorial/tkinter-tutorial/tkinter-geometry-managers/#tkinter-grid-%25E4%25BD%2588%25E5%25B1%2580%25E6%2596%25B9%25E6%25B3%2595

from Willy_Modules import *


import tkinter as tk
from pytube import YouTube
def clickUrl():  # 按「確定」鈕後處理函式 (btnUrl)
    global list_video, list_radio, yt
    for r in list_radio:  # 移除選項按鈕
        r.destroy()
    list_radio.clear()  # 清除串列
    list_video.clear()
    labelMsg.config(text="")  # 清除提示訊息
    labelMsg.config(text="以下為選擇下載影片之畫質與檔案類型\n")
    if url.get() == "":  # 若未輸入網址就顯示提示訊息
        labelMsg.config(text="網址欄位必須輸入！")
    else:
        try:  # 捕捉影片不存在的錯誤
            # yt.url = url.get()  # 取得輸入網址
            yt = YouTube(url.get())
            print(url.get())
            rbvalue = 1  # 設定選項按鈕的值
            entry_File.config(state="normal")
            filename.set(yt.title)  # 取得影片名稱
            entry_File.config(state="disabled")
            for v1 in yt.streams.filter(progressive=True).all():  # 建立影片格式串列
                list_video.append(v1)
            for v2 in list_video:  # 迴圈建立多個影片格式選項按鈕
                # 這個元件就是常見的按圓形按紐，通常不能複選。
                rbtem = tk.Radiobutton(frame3, text=v2,
                                       variable=video,
                                       value=rbvalue,
                                       command=rbVideo)
#                if(rbvalue==1):  # 預設選取第1個選項按鈕
#                    rbtem.select()
#                    rbVideo()
                list_radio.append(rbtem)  # 建立選項按鈕串列
                rbtem.grid(row=rbvalue-1, column=0,
                           sticky="w")
                rbvalue += 1
            btnDown.config(state="normal")  # 設定「下載影片」按鈕有效
            btnDown2.config(state="normal")
        except:  # 顯示影片不存在訊息
            for r in list_radio:  # 移除選項按鈕
                r.destroy()
            list_radio.clear()  # 清除串列
            list_video.clear()
            labelMsg.config(text="找不到此YouTube！\n正確格式應為https://www.youtube.com/watch?v=XXXXX...")


def rbVideo():  # 點選選項按鈕後處理函式 (rbtem: Radiobutton)
    global get_video, str_ftype, str_video
    labelMsg.config(text="")
    str_video = str(list_video[video.get()-1])  # 取得點選項目
    # 取得影片型態(Ex.mp4、3gpp)
    start1 = str_video.find("video/")
    end1 = str_video.find("res")
    str_ftype = str_video[start1+6 : end1-2]
    # 取得影片解析度(Ex.360p、240p)
    end2 = str_video.find("fps")
    strresolution = str_video[end1+5 : end2-2]
    get_video = yt.streams.filter(subtype=str_ftype, resolution=strresolution).first()  # 取得影片格式
    print(str_ftype, strresolution)



def clickDown():  # 按「下載影片」鈕後處理函式 (btnDown)
    global get_video, str_ftype, list_radio
    if(path.get()==""):  # 若未輸入路徑就顯示提示訊息
        labelMsg.config(text="路徑欄位必須輸入！")
    else:
        labelMsg.config(text="")
        fpath = path.get()  # 取得輸入存檔資料夾
        fpath = fpath.replace("\\", "\\\\")
                                # 將「\」轉換為「\\」
#    yt.set_filename(filename.get())
        get_video.download(fpath)
        for r in list_radio:  # 移除選項按鈕
            r.destroy()
        list_radio.clear()  # 清除串列
        list_video.clear()
        url.set("")  # 清除輸入框
        filename.set("")
        btnDown.config(state="disabled")
        btnDown2.config(state="disabled")


def cd():  # 按「下載音樂」鈕後處理函式 (btnDown2)
    global get_video, str_ftype, list_radio
    if(path.get()==""):  # 若未輸入路徑就顯示提示訊息
        labelMsg.config(text="路徑欄位必須輸入！")
    else:
        labelMsg.config(text="")
        fpath = path.get()  # 取得輸入存檔資料夾
        fpath = fpath.replace("\\", "\\\\")
        yt.streams.get_by_itag(140).download(fpath)
        for r in list_radio:  # 移除選項按鈕
            r.destroy()
        list_radio.clear()  # 清除串列
        list_video.clear()
        url.set("")  # 清除輸入框
        filename.set("")
        btnDown.config(state="disabled")
        btnDown2.config(state="disabled")




win = tk.Tk() # GUI的核心，需要用這個函式建立架構
win.title("YouTube_Downloader_Python") #
win.geometry("600x400")  # 設定主視窗解析度(長寬設定)

get_video = ""  # 影片格式
str_ftype = ""  # 影片型態
list_video = []  # 影片格式串列
list_radio = []  # 選項按鈕串列
video = tk.IntVar()  # 選項按鈕值
url = tk.StringVar()  # 影片網址 (entry_Url)
path = tk.StringVar()  # 存檔資料夾 (entry_Path)
filename = tk.StringVar()  # 存檔名稱 (entry_File)


frame1 = tk.Frame(win, width=450)
# 在tkinter中，有三種佈局，分別是pack、grid以及place
frame1.pack(side="top")  # 其中pack為最基礎的佈局方式

# 可以想像成是一個空的盒子，可以放入你想要的東西
# 如果要使用image函式來塞圖片，先用tk.PhotoImage()這個功能選取圖片後，再丟到Label中
label1 = tk.Label(frame1, text="YouTube Url: ")
# Entry用來呈現讓使用者輸入文字的視窗，利用show()函式可以將輸入的文字轉成指定的文字
entry_Url = tk.Entry(frame1, textvariable=url)
entry_Url.config(width=50)
# button這個元件就是按鈕，比較重要的參數就是text，用來顯示按鈕內的文字。
btnUrl = tk.Button(frame1, text="Scrape!", command=clickUrl)
# grid可以想像成是表格式的排列方法，可以利用控制row(列)以及column(行)來有規律地規劃元素
label1.grid(row=0, column=0, pady=10, sticky="e")
entry_Url.grid(row=0, column=1)
btnUrl.grid(row=0, column=2)


label2 = tk.Label(frame1, text="Folder Path to Save File: ")
entry_Path = tk.Entry(frame1, textvariable=path)
entry_Path.config(width=50)
label2.grid(row=1, column=0, pady=10, sticky="e")
entry_Path.grid(row=1, column=1)


label3 = tk.Label(frame1, text="File Name: ")
entry_File = tk.Entry(frame1, textvariable=filename)
entry_File.config(width=50)
label3.grid(row=2, column=0, pady=10, sticky="e")
entry_File.grid(row=2, column=1)


label4 = tk.Label(frame1, fg="blue", font=10,
                  text="程式會停頓代表在執行中，並非當掉！")
label4.grid(row=3, column=1, columnspan=2, sticky="se")




frame2 = tk.Frame(win)
frame2.pack()

btnDown2 = tk.Button(frame2, text="Download Music", command=cd)
btnDown2.pack(pady=6)
btnDown2.config(state="disabled")  # 開始時設定「下載音樂」按鈕無效
btnDown = tk.Button(frame2, text="Download Video", command=clickDown)
btnDown.pack(pady=6)
btnDown.config(state="disabled")  # 開始時設定「下載影片」按鈕無效

labelMsg = tk.Label(frame2, text="", fg="red")  # 訊息標籤
labelMsg.pack()




frame3 = tk.Frame(win)  # 選項按鈕區塊
frame3.pack()




win.mainloop()  # 非常重要的函式，會使程式常駐執行
