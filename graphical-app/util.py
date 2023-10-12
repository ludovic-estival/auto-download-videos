import os
import tkinter as tk
from pytube import YouTube
from tkinter import filedialog

"""
Download video or audio from YouTube links.

textField: tkinter Text widget with YouTube links inside
videoFormat: "MP3" or "MP4"
"""
def downloadVideo(textField, videoFormat):
    folderSelected = filedialog.askdirectory()
    textContent = textField.get("1.0", "end-1c")

    if folderSelected == "" or textContent == "":
        return

    errorNb = 0
    videoList = textContent.split()

    for link in videoList:
        try:
            yt = YouTube(link)

            if videoFormat == "MP3":
                audio = yt.streams.filter(only_audio=True).first()
                outFile = audio.download(output_path=folderSelected)
                base, extension = os.path.splitext(outFile)
                newFile = base + '.mp3'
                os.rename(outFile, newFile)
            else:
                video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(folderSelected)

        except:
            errorNb += 1
            continue

    message = str(len(videoList)) + " fichiers téléchargés." + str(errorNb) + " erreur(s) rencontrée(s)."
    tk.messagebox.showinfo("Téléchargement terminé", message)