# -*- coding: utf-8 -*-

# https://ithelp.ithome.com.tw/users/20140047/ironman/4481
# https://vocus.cc/article/624e6738fd89780001ae7c1e
# https://ithelp.ithome.com.tw/articles/10278264
# https://www.delftstack.com/zh-tw/tutorial/tkinter-tutorial/tkinter-geometry-managers/#tkinter-grid-%25E4%25BD%2588%25E5%25B1%2580%25E6%2596%25B9%25E6%25B3%2595
# https://www.tutorialspoint.com/python/tk_entry.htm#
# https://stackoverflow.com/questions/20125967/how-to-set-default-text-for-a-tkinter-entry-widget
# https://tw.coderbridge.com/series/c471d97bb201460ab137c5e4955987df/posts/0baeb8bf25e543ed8462bd742cd1946f
# https://pytube.io/en/latest/user/streams.html
# https://www.pythontutorial.net/tkinter/tkinter-grid/
# https://stackoverflow.com/questions/65635835/displaying-image-from-url-in-python-tkinter
# https://stackoverflow.com/questions/60664217/how-do-i-setup-a-window-icon-using-tkinter
# https://stackoverflow.com/questions/64770422/how-to-display-image-in-python-tkinter-from-url

# from Willy_Modules import *
import tkinter as tk
from pytube import YouTube
import urllib.request
from PIL import ImageTk, Image
import io

### 自建函數
def clickUrl():  # 按「Scrape」鈕後處理函式 (btnUrl)
    global list_video, list_radio, yt
    for r in list_radio:  # 移除選項按鈕
        r.destroy()
    list_radio.clear()  # 清除串列
    list_video.clear()
    # labelMsg.config(text="")  # 清除提示訊息
    labelMsg.config(text="Select file format and video resolution\n")
    if url.get() == "":  # 若未輸入網址就顯示提示訊息
        labelMsg.config(text="No value in YouTube Url!")
    else:
        # 捕捉影片不存在的錯誤
        try:  # 顯示影片存在訊息
            # yt.url = url.get()  # 取得輸入網址
            yt = YouTube(url.get())
            print(url.get())
            rbvalue = 1  # 設定選項按鈕的值
            # entry_File.config(state="normal")  # Editable
            # entry_File.config(state="disabled")  # Uneditable
            for v1 in yt.streams.filter(progressive=True):  # 建立影片格式串列 .all() is deprecated
                list_video.append(v1)
            # for v1 in yt.streams:  # 建立影片格式串列 .all() is deprecated
            #     list_video.append(v1)
            for v2 in list_video:  # 迴圈建立多個影片格式選項按鈕
                # 這個元件就是常見的按圓形按紐，通常不能複選。
                rbtem = tk.Radiobutton(frame3, text=v2,
                                       variable=video,
                                       value=rbvalue,
                                       command=rbVideo)
                # if rbvalue == 1:  # 預設選取第1個選項按鈕
                #     rbtem.select()
                #     rbVideo()
                list_radio.append(rbtem)  # 建立選項按鈕串列
                rbtem.grid(row=rbvalue-1, column=0, sticky="w")
                rbvalue += 1
            list_radio[-1].select()  # 預設選取最後1個選項按鈕
            rbVideo()  # 點選選項按鈕後處理函式
            # filename.set(yt.title)  # 取得影片名稱
            btnDown.config(state="normal")  # 設定「下載影片」按鈕有效
            btnDown2.config(state="normal")
        except:  # 顯示影片不存在訊息
            for r in list_radio:  # 移除選項按鈕
                r.destroy()
            list_radio.clear()  # 清除串列
            list_video.clear()
            labelMsg.config(text="Cannot find the YouTube Url!\nThe correct url format should be:\nhttps://www.youtube.com/watch?v=XXXXXX......\nor\nhttps://youtu.be/XXXXXX")


def rbVideo():  # 點選選項按鈕後處理函式 (rbtem: Radiobutton)
    global get_video, str_ftype, str_video, full_filename
    labelMsg.config(text="")
    str_video = str(list_video[video.get()-1])  # 取得點選項目
    print(video, str_video)
    # 取得影片型態 (Ex. mp4、3gpp)
    start1 = str_video.find("video/")
    end1 = str_video.find("res")
    str_ftype = str_video[start1+6:end1-2]
    # 取得影片解析度 (Ex. 720p、360p、240p)
    end2 = str_video.find("fps")
    str_resolution = str_video[end1+5:end2-2]
    get_video = yt.streams.filter(subtype=str_ftype, resolution=str_resolution).first()  # 取得影片格式
    print(str_ftype, str_resolution)
    full_filename = yt.title+"_"+str_ftype+"_"+str_resolution
    full_filename = full_filename.replace("/", "_").replace("\\", "_").replace(":", "_")
    filename.set(full_filename)  # 取得影片名稱


def clickDown():  # 按「Download Video」鈕後處理函式 (btnDown)
    global get_video, str_ftype, list_radio
    if path.get() == "":  # 若未輸入路徑就顯示提示訊息
        labelMsg.config(text="No value in Folder Path!")
    else:
        labelMsg.config(text="")
        fpath = path.get()  # 取得輸入存檔資料夾
        fpath = fpath.replace("\\", "\\\\")
        # 將「\」轉換為「\\」
        #    yt.set_filename(filename.get())
        get_video.download(skip_existing=False, output_path=fpath, filename=full_filename+"."+full_filename.split("_")[-2])
        # for r in list_radio:  # 移除選項按鈕
        #     r.destroy()
        # list_radio.clear()  # 清除串列
        # list_video.clear()
        # url.set("")  # 清除輸入框
        # filename.set("")
        # btnDown.config(state="disabled")
        # btnDown2.config(state="disabled")
        labelMsg.config(text="Done!")


def cd():  # 按「Download Music」鈕後處理函式 (btnDown2)
    global get_video, str_ftype, list_radio
    if path.get() == "":  # 若未輸入路徑就顯示提示訊息
        labelMsg.config(text="No value in Folder Path!")
    else:
        labelMsg.config(text="")
        fpath = path.get()  # 取得輸入存檔資料夾
        fpath = fpath.replace("\\", "\\\\")
        yt.streams.get_by_itag(140).download(skip_existing=False, output_path=fpath, filename=yt.title.replace("/", "_").replace("\\", "_").replace(":", "_")+"_music.mp4")
        # for r in list_radio:  # 移除選項按鈕
        #     r.destroy()
        # list_radio.clear()  # 清除串列
        # list_video.clear()
        # url.set("")  # 清除輸入框
        # filename.set("")
        # btnDown.config(state="disabled")
        # btnDown2.config(state="disabled")
        labelMsg.config(text="Done!")


### 主程式
win = tk.Tk()  # GUI的核心，需要用這個函式建立架構
win.title("YouTube_Downloader_Python")  #
win.geometry("1000x400")  # 設定主視窗解析度(長寬設定)

url = 'https://raw.githubusercontent.com/LeBronWilly/YouTube_Downloader_Python/main/YouTube.png'
img_data = urllib.request.urlopen(url).read()
image = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
win.iconphoto(False, image)

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
entry_Url.config(width=100)
# button這個元件就是按鈕，比較重要的參數就是text，用來顯示按鈕內的文字。
btnUrl = tk.Button(frame1, text="Scrape!", command=clickUrl)
# grid可以想像成是表格式的排列方法，可以利用控制row(列)以及column(行)來有規律地規劃元素
label1.grid(row=0, column=0, pady=10, sticky="e")
entry_Url.grid(row=0, column=1)
btnUrl.grid(row=0, column=2)

label2 = tk.Label(frame1, text="Folder Path to Save File: ")
entry_Path = tk.Entry(frame1, textvariable=path)
entry_Path.config(width=100)
entry_Path.insert(-1, 'Download/')
# path.set("Download")
label2.grid(row=1, column=0, pady=10, sticky="e")
entry_Path.grid(row=1, column=1)

label3 = tk.Label(frame1, text="File Name: ")
entry_File = tk.Entry(frame1, textvariable=filename)
entry_File.config(width=100, state="disabled")  # Uneditable
label3.grid(row=2, column=0, pady=10, sticky="e")
entry_File.grid(row=2, column=1)

label4 = tk.Label(frame1, fg="blue",
                  text="                          \
                  When executing, the program will pause, not crash!")
label4.grid(row=3, column=1, columnspan=1, sticky="w")



frame2 = tk.Frame(win)
frame2.pack()

btnDown2 = tk.Button(frame2, text="Download Music", command=cd)
btnDown2.pack(pady=6)
btnDown2.config(state="disabled")  # 開始時設定「下載音樂」按鈕無效

label5 = tk.Label(frame2, text="===============================================================================")  # 訊息標籤
label5.pack()


frame3 = tk.Frame(win)  # 選項按鈕區塊
frame3.pack()
btnDown = tk.Button(frame2, text="Download Video", command=clickDown)
btnDown.pack(pady=6)
btnDown.config(state="disabled")  # 開始時設定「下載影片」按鈕無效


labelMsg = tk.Label(frame2, text="Welcome!", fg="red")  # 訊息標籤
labelMsg.pack()

win.mainloop()  # 非常重要的函式，會使程式常駐執行
