# A DEPLACE
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
from tkinter import ttk

window = Tk()
window.geometry("600x300")
window.title("Video Downloader")
window.iconbitmap("assets\\icon.ico")

# -- Grid
#window.columnconfigure(0, weight=3)
#window.rowconfigure(1, weight=2)
#window.columnconfigure(1, weight=1)
#window.columnconfigure(2, weight=1)

# -- Text Field
#Label(window, text="Un lien par ligne.", font=("Arial", 11), justify="left").pack(anchor=W)
urlText = tk.Text(window, height=8, width=40)
#scroll = tk.Scrollbar(window)
#urlText.configure(yscrollcommand=scroll.set)
#urlText.pack()
#scroll.config(command=urlText.yview) 
#scroll.pack(side=RIGHT, fill=Y)

urlText.grid(column=0, row=0, rowspan=2, sticky=tk.W, padx=5, pady=5)
# --

videoFormat = StringVar(value="MP3")
Radiobutton(window, text="Audio (MP3)", variable=videoFormat, value="MP3", font=("Arial", 11)).grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)
Radiobutton(window, text="Audio + vidéo (MP4)", variable=videoFormat, value="MP4", font=("Arial", 11)).grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

urlButton = Button(window, text="Valider", command=validateUrl, font=("Arial", 11)).grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

window.mainloop()