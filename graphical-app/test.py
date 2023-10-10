from tkinter import *
from tkinter import ttk

root = Tk()
content = ttk.Frame(root)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


urlText = Text(content, height=8, width=40)

videoFormat = StringVar(value="MP3")

mp3Radio = ttk.Radiobutton(content, text="Audio (MP3)", variable=videoFormat, value="MP3")
mp4Radio = ttk.Radiobutton(content, text="Audio + vidéo (MP4)", variable=videoFormat, value="MP4")

aide = ttk.Button(content, text="Aide", command=lambda: print("aide en cours"))
ok = ttk.Button(content, text="Valider", command=lambda: print(urlText.compare('end-1c', "==", "1.0"))) 

content.grid(column=0, row=0)

urlText.grid(column=0, row=0, columnspan=3, rowspan=2)

mp3Radio.grid(column=0, row=3)
mp4Radio.grid(column=1, row=3)
aide.grid(column=4, row=0)
ok.grid(column=2, row=4)

root.mainloop()