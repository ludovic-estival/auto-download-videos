videosLinks = ["https://www.youtube.com/watch?v=Pvf6uqNb_Lc"]
destination = r'D:\users\Trahald\Desktop'

from pytube import YouTube
import os

for video in videosLinks:
    yt = YouTube(str(video))
    v = yt.streams.filter(only_audio=True).first()
    out_file = v.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
