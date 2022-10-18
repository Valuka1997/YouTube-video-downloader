import tkinter.font as tkFont
from pytube import YouTube
import pytube
import os
import urllib.request
import json
import urllib
from tkinter import *
from tkinter import messagebox
import re
import pyperclip


def info():
    messagebox.showinfo("Info","You Can Paste the YouTube video URL and download the file in to the folder which contains the program")

def paste():
    lnk = pyperclip.paste()
    link.delete(0, END)
    link.insert(0, lnk)


def download():
    print("abcabc")
    if len(link.get()) != 0:
        params = {"format": "json", "url": "%s" % link.get()}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string


        try:
            with urllib.request.urlopen(url) as response:
                response_text = response.read()
                data = json.loads(response_text.decode())
                title = (data['title'])
        except urllib.error.HTTPError as exception:
            messagebox.showwarning(title="Error", message="Requested URL not found")
            ui.mainloop()

        #downloading the video
        name = pytube.extract.video_id(link.get())
        YouTube(link.get()).streams.filter(only_audio=True).first().download(filename=name)

        #grabbing the current working directory
        path = os.getcwd() + '\\'

        #get the location and name of the downloaded file
        location = path + name
        fmtitle = re.sub(r"[^a-zA-Z0-9]"," ",title)
        nwname = path + fmtitle + '.mp4'

        #renaming existing file to mp4
        os.rename(location, nwname)

    else:
        messagebox.showinfo("info", "Please enter a valid URL to continue")

root = Tk()
#setting title
root.title("YouTube Audio downloader")
#setting window size
width=350
height=250
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

download_button=Button(root)
download_button["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
download_button["font"] = ft
download_button["fg"] = "#000000"
download_button["justify"] = "center"
download_button["text"] = "Button"
download_button.place(x=90,y=170,width=173,height=48)
download_button["command"] = download

link=Entry(root)
link["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
link["font"] = ft
link["fg"] = "#333333"
link["justify"] = "center"
link["text"] = "Enter Youtube Link"
link.place(x=20,y=90,width=280,height=42)

pstbtn=Button(root)
ft = tkFont.Font(family='Times',size=10)
pstbtn["font"] = ft
pstbtn["fg"] = "#000000"
pstbtn["justify"] = "center"
pstbtn["text"] = "Paste"
pstbtn.place(x=305,y=90,width=32,height=42)
pstbtn["command"] = paste
title1=Label(root)
ft = tkFont.Font(family='Times',size=10)
title1["font"] = ft
title1["fg"] = "#333333"
title1["justify"] = "center"
title1["text"] = "YouTube Video Downloader"
title1.place(x=40,y=30,width=250,height=25)

infobtn=Button(root)
infobtn["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
infobtn["font"] = ft
infobtn["fg"] = "#000000"
infobtn["justify"] = "center"
infobtn["text"] = "info"
infobtn.place(x=310,y=210,width=32,height=30)
infobtn["command"] = info

root.mainloop()
