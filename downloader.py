from pytube import YouTube
from pprint import pprint
from tkinter import *
from tkinter.ttk import *
import tkinter.filedialog
from tkinter import messagebox

window = Tk()
window.title("YouTube Downloader")
VIDEO_URL = ""
video = None
combo_var = StringVar()
SAVING_DIRECTORY=""
video_list =Combobox(window, textvariable=combo_var)

def onFetchURLPressed():
    global VIDEO_URL
    VIDEO_URL = name.get()
    global video
    video = YouTube(VIDEO_URL)
    list_videos = []
    for i in video.streams.filter(progressive=True):
        list_videos.append(i.resolution)
    video_list['values'] = list_videos
    video_list.current(0)
    video_list.grid(row=2, column=0, columnspan=3)
    get_directory_button.grid(row=3, column=0, columnspan=3)

def onGetDirectoryButtonPressed():
    directory_path = tkinter.filedialog.askdirectory()
    global SAVING_DIRECTORY
    SAVING_DIRECTORY = directory_path
    dowload_button.grid(row=4, column=0, columnspan=3)

def onDownloadPressed():
    video.streams.get_by_resolution(combo_var.get()).download(output_path=SAVING_DIRECTORY+"/")

url_label = Label(window, text="URL")
url_label.grid(row=0, column=0)

name = StringVar()
nameEntered = Entry(window, textvariable = name)
nameEntered.grid(row = 0, column = 1)

fetch_url_button = Button(window, text="Get Video", command=onFetchURLPressed)
fetch_url_button.grid(row=1, column=0, columnspan=3)

get_directory_button = Button(window, text="Select Directory", command=onGetDirectoryButtonPressed)

dowload_button = Button(window, text="Download", command=onDownloadPressed)
window.mainloop()
