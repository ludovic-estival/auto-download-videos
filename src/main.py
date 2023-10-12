from tkinter import *
from tkinter import ttk
from util import downloadVideo

root = Tk()
root.title("Video Downloader")

videoFormat = StringVar(value="MP3")

urlText = Text(root, height=8, width=40)
mp3Radio = ttk.Radiobutton(root, text="Audio (MP3)", variable=videoFormat, value="MP3")
mp4Radio = ttk.Radiobutton(root, text="Audio + vidéo (MP4)", variable=videoFormat, value="MP4")
aide = ttk.Button(root, text="Aide", command=lambda: print("aide en cours"))
ok = ttk.Button(root, text="Valider", command=lambda: downloadVideo(urlText, videoFormat.get()))

urlText.pack(anchor=NW, ipadx=100)
mp3Radio.pack(expand=True, side=LEFT, fill=BOTH)
mp4Radio.pack(expand=True, side=LEFT, fill=BOTH)
aide.pack(expand=True, side=LEFT, fill=BOTH)
ok.pack(expand=True, side=LEFT, fill=BOTH)

root.mainloop()