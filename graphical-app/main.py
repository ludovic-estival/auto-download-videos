urlLabel = "Saisir le lien d'une ou plusieurs vidéos.\nDans le cas de plusieurs vidéos, saisir un lien par ligne."

def validateUrl():
    folderSelected = filedialog.askdirectory()
    value = urlText.get("1.0", "end-1c")

    if folderSelected == "":
        return

    if value != "":
        errorNb = 0
        videoList = value.splitlines()
        
        for link in videoList:
            try:
                yt = YouTube(link)

                if videoFormat.get() == "MP3":
                    video = yt.streams.filter(only_audio=True).first()
                    outFile = video.download(output_path=folderSelected)
                    base, extension = os.path.splitext(outFile)
                    newFile = base + '.mp3'
                    os.rename(outFile, newFile)
                else:
                    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(folderSelected)

            except Exception as error:
                errorNb += 1
                continue
    else:
        tk.messagebox.showinfo("Problème rencontré",  "Il faut au moins un lien.")

    mssg = str(len(videoList)) + " vidéo(s) téléchargée(s). " + str(errorNb) + " erreur(s) rencontrée(s)."
    tk.messagebox.showinfo("Téléchargement terminé",  mssg)

from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *

window = tk.Tk()
window.title("Video Downloader")

videoFormat = StringVar(value="MP3")
Radiobutton(window, text="MP3", variable=videoFormat, value="MP3").pack(anchor=W)
Radiobutton(window, text="MP4", variable=videoFormat, value="MP4").pack(anchor=W)
Label(window, text=urlLabel, font=("Arial", 11), justify="left").pack(anchor=W)

# -- Text Field
urlText = tk.Text(window, height=8, width=40)
scroll = tk.Scrollbar(window)
urlText.configure(yscrollcommand=scroll.set)
urlText.pack()
scroll.config(command=urlText.yview) 
scroll.pack(side=RIGHT, fill=Y)
# --

urlButton = Button(window, text="Valider", command=validateUrl, font=("Arial", 11)).pack()

window.mainloop()