def clickUrl():  #按「確定」鈕後處理函式
    global listvideo, listradio , yt
    for r in listradio:  #移除選項按鈕
        r.destroy()
    listradio.clear()  #清除串列
    listvideo.clear()
    labelMsg.config(text="")  #清除提示訊息
    labelMsg.config(text="以下為選擇下載影片之畫質與檔案類型\n")
    if(url.get()==""):  #若未輸入網址就顯示提示訊息
        labelMsg.config(text="網址欄位必須輸入！")
    else:
        try:  #捕捉影片不存在的錯誤
#            yt.url = url.get()  #取得輸入網址
            yt = YouTube(url.get())
            print(url.get())
            rbvalue = 1  #設定選項按鈕的值
            entryFile.config(state="normal")
            filename.set(yt.title)  #取得影片名稱
            entryFile.config(state="disabled")
            for v1 in yt.streams.filter(progressive=True).all():  #建立影片格式串列
                listvideo.append(v1)
            for v2 in listvideo:  #迴圈建立多個影片格式選項按鈕
                rbtem = tk.Radiobutton(frame3, text=v2, 
                                       variable=video, 
                                       value=rbvalue, 
                                       command=rbVideo)
#                if(rbvalue==1):  #預設選取第1個選項按鈕
#                    rbtem.select()
#                    rbVideo()
                listradio.append(rbtem)  #建立選項按鈕串列        
                rbtem.grid(row=rbvalue-1, column=0, 
                           sticky="w")
                rbvalue += 1
            btnDown.config(state="normal")  #設定「下載影片」按鈕有效
            btnDown2.config(state="normal")
        except:  #顯示影片不存在訊息
            for r in listradio:  #移除選項按鈕
                r.destroy()
            listradio.clear()  #清除串列
            listvideo.clear()
            labelMsg.config(text="找不到此YouTube！\n正確格式應為https://www.youtube.com/watch?v=XXXXX...")
        
        
def rbVideo():  #點選選項按鈕後處理函式
    global getvideo, strftype, strvideo
    labelMsg.config(text="")
    strvideo = str(listvideo[video.get()-1])  #取得點選項目
    #取得影片型態(Ex.mp4、3gpp)
    start1 = strvideo.find("video/")
    end1 = strvideo.find("res")
    strftype = strvideo[start1+6 : end1-2]
    #取得影片解析度(Ex.360p、240p)
    end2 = strvideo.find("fps")
    strresolution = strvideo[end1+5 : end2-2]
    getvideo = yt.streams.filter(subtype=strftype, resolution=strresolution).first()  #取得影片格式
    print(strftype, strresolution)
        
    
    
def clickDown():  #按「下載影片」鈕後處理函式
    global getvideo, strftype, listradio
    if(path.get()==""):  #若未輸入路徑就顯示提示訊息
        labelMsg.config(text="路徑欄位必須輸入！")
    else:
        labelMsg.config(text="")
        fpath = path.get()  #取得輸入存檔資料夾
        fpath = fpath.replace("\\", "\\\\")  
                                #將「\」轉換為「\\」
#    yt.set_filename(filename.get())
        getvideo.download(fpath)
        for r in listradio:  #移除選項按鈕
            r.destroy()
        listradio.clear()  #清除串列
        listvideo.clear()
        url.set("")  #清除輸入框
        filename.set("")
        btnDown.config(state="disabled")  
        btnDown2.config(state="disabled")


def cd():  #按「下載音樂」鈕後處理函式
    global getvideo, strftype, listradio
    if(path.get()==""):  #若未輸入路徑就顯示提示訊息
        labelMsg.config(text="路徑欄位必須輸入！")
    else:
        labelMsg.config(text="")
        fpath = path.get()  #取得輸入存檔資料夾
        fpath = fpath.replace("\\", "\\\\")
        yt.streams.get_by_itag(140).download(fpath)
        for r in listradio:  #移除選項按鈕
            r.destroy()
        listradio.clear()  #清除串列
        listvideo.clear()
        url.set("")  #清除輸入框
        filename.set("")
        btnDown.config(state="disabled")
        btnDown2.config(state="disabled")


import tkinter as tk
from pytube import YouTube

win=tk.Tk()
win.geometry("600x400")  #設定主視窗解析度
win.title("YouTube Downloader__LeBron-Willy Fang（方聖瑋）")

getvideo = ""  #影片格式
strftype = ""  #影片型態
listvideo = []  #影片格式串列
listradio = []  #選項按鈕串列
video = tk.IntVar()  #選項按鈕值
url = tk.StringVar()  #影片網址
path = tk.StringVar()  #存檔資料夾
filename = tk.StringVar()  #存檔名稱


frame1 = tk.Frame(win, width=450)
frame1.pack()
label1=tk.Label(frame1, text="YouTube網址：")
entryUrl = tk.Entry(frame1, textvariable=url)
entryUrl.config(width=40)

btnUrl = tk.Button(frame1, text="爬取！", command=clickUrl)
label1.grid(row=0, column=0, sticky="e")
entryUrl.grid(row=0, column=1)
btnUrl.grid(row=0, column=2)

label2=tk.Label(frame1, text="存檔路徑資料夾：")
entryPath = tk.Entry(frame1, textvariable=path)
entryPath.config(width=40)
label2.grid(row=1, column=0, pady=6, sticky="e")
entryPath.grid(row=1, column=1)

label3=tk.Label(frame1, text="名稱顯示：")
entryFile = tk.Entry(frame1, textvariable=filename)
entryFile.config(width=40)
label3.grid(row=2, column=0, pady=3, sticky="e")
entryFile.grid(row=2, column=1)

label4=tk.Label(frame1, fg="blue", font=(12),
                text="下載速度視電腦而定，音樂會稍慢些\n程式會停頓代表在執行中，並非當掉！\n")
label4.grid(row=3, column=1, columnspan=2,sticky="se")


frame2 = tk.Frame(win)
frame2.pack()

btnDown2 = tk.Button(frame2, text="僅下載音樂", command=cd)
btnDown2.pack(pady=6)
btnDown2.config(state="disabled")  #開始時設定「下載音樂」按鈕無效
btnDown = tk.Button(frame2, text="下載影片", command=clickDown)
btnDown.pack(pady=6)
btnDown.config(state="disabled")  #開始時設定「下載影片」按鈕無效

labelMsg = tk.Label(win, text="", fg="red")  #訊息標籤
labelMsg.pack()

frame3 = tk.Frame(win)  #選項按鈕區塊
frame3.pack()
    
win.mainloop()
