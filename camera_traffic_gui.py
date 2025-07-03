
url = ""#ライブカメラのURL
import os

def rmQ(fname):
    return fname.split("?")[0] #保存するファイル名から「？」以下を削除

def getImgURL(src, url):
    if "http" not in src:
        return url+src #他ページからのリンクに対応
    else:
        return src

def mkdir(dirName):
    try:
        os.mkdir(dirName) #ディレクトリ作成
    except Exception as e:
        print (e)
#        pass # if dirName already exist

def DLImages(AllImages, url, dirName):
    import urllib

    successNum = 0
    for img in AllImages:
        src = img.get("src") #imgタグのsrcを取得
        imgURL = getImgURL(src, url)
        fname = src.split("/")[-1]

        if "?" in fname:
            fname = rmQ(fname)
        try:
            if fname in os.listdir(dirName):
                fname = fname + str(successNum)
            urllib.request.urlretrieve(imgURL, dirName+"/"+fname) #作成したディレクトリに保存
            print ("[ Success ] " + imgURL)
            successNum += 1
        except Exception as e:
            print (e)
            print ("[ Failed ] " + imgURL)

    return successNum #ダウンロード成功の数を返す

def main(url, dirName="../py"):
	from bs4 import BeautifulSoup
	import urllib.request
	import tkinter as tk
	from PIL import Image, ImageTk # ← 追加
	
	root = tk.Tk()
	print(root.geometry())
	root.geometry('400x250+0+0')
	
	canvas = tk.Canvas(
	root,               # 親要素をメインウィンドウに設定
	width = 500,        # 幅を設定
	height = 300,       # 高さを設定
	relief=tk.RIDGE,    # 枠線を表示
	bd=0                # 枠線の幅を設定
	)
	canvas.place(x=0, y=0)                # メインウィンドウ上に配置

	
	mkdir(dirName)
	response = urllib.request.urlopen(url) #ページオープン
	html = response.read() #html取得
	soup = BeautifulSoup(html,"html.parser")
	AllImages = soup.find_all("img") #全imgタグを取得
	imgNum = len(AllImages)
	successNum = DLImages(AllImages, url, dirName)
	
	print (successNum, "images could be downloaded (in", imgNum, "images).")
	
	img = ImageTk.PhotoImage(file = 'tenc.jpg')  # 表示するイメージを用意
	canvas.create_image(                    # キャンバス上にイメージを配置
	0,                                  # x座標
	0,                                  # y座標
	image = img,                        # 配置するイメージオブジェクトを指定
	anchor = tk.NW                      # 配置の起点となる位置を左上隅に指定
	)
	
	os.remove("tenc.jpg")
	root.mainloop()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
		
"""

import requests
import youtube_dl

query = "日本語ラップ選手権"

page = 0
limit = 1

SERCH_URL = "http://youtube.com{}".format(query,page,limit)

res = requests.get(SERCH_URL).json()
if res["succcess"]:
	target_url = res["response"]["videos"]["video_url"]
	ydl_opts = {}
	
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download
		

"""