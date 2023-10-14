from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import filedialog
import os

def downloadVideo(textField, videoFormat, label):
    folderSelected = filedialog.askdirectory()
    textContent = textField.get("1.0", "end-1c")

    if folderSelected == "" or textContent == "":
        return

    videoList = textContent.split()

    for link in videoList:
        yt = YouTube(link)
        text = "\n" + yt.title + " : "
        label["text"] += text

        try:
            
            if videoFormat == "MP3":
                audio = yt.streams.filter(only_audio=True).first()
                outFile = audio.download(output_path=folderSelected)
                base, extension = os.path.splitext(outFile)
                newFile = base + '.mp3'
                os.rename(outFile, newFile)
            else:
                video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(folderSelected)
            
            label["text"] += "terminé"
    
        except Exception as error:
            print(error)
            label["text"] += "erreur"
            continue

root = Tk()
root.title("Video Downloader")

videoFormat = StringVar(value="MP3")

# -- Widget creation
dlFrame = ttk.Frame(root, relief="solid", borderwidth="5")
dlTitle = ttk.Label(dlFrame, text="Téléchargements:", font=("Arial", 11))
dlVideos = ttk.Label(dlFrame, text="Saisir un ou plusieurs liens et valider.")
urlText = Text(root, height=8, width=40)
mp3Radio = ttk.Radiobutton(root, text="Audio (MP3)", variable=videoFormat, value="MP3")
mp4Radio = ttk.Radiobutton(root, text="Audio + vidéo (MP4)", variable=videoFormat, value="MP4")
aide = ttk.Button(root, text="Aide", state="disabled")
ok = ttk.Button(root, text="Valider", command=lambda: downloadVideo(urlText, videoFormat.get(), dlVideos))

# -- Widget display
dlFrame.pack(anchor=NE, side=RIGHT)
dlTitle.pack()
dlVideos.pack()
urlText.pack(anchor=NW, ipadx=100, ipady=50)
mp3Radio.pack(side=LEFT, fill=BOTH, ipadx=10)
mp4Radio.pack(side=LEFT, fill=BOTH, ipadx=10)
aide.pack(side=LEFT, fill=BOTH, ipadx=10)
ok.pack(side=LEFT, fill=BOTH, ipadx=10)

root.mainloop()