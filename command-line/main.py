# Download all videos in "videosLinks" in the MP3 format
# Files are saved in the "destination" folder

videosLinks = ["https://www.youtube.com/watch?v=w-sQRS-Lc9k&list=PLLQx3KNygnh8ADwbu3vo4mfYbWMUUfCSG&index=1&pp=gAQBiAQB8AUB",
               "https://www.youtube.com/watch?v=hkij4LvACZ0&list=PLLQx3KNygnh8ADwbu3vo4mfYbWMUUfCSG&index=2&pp=gAQBiAQB8AUB",
               "https://www.youtube.com/watch?v=dM4llS865Bg&list=PLLQx3KNygnh8ADwbu3vo4mfYbWMUUfCSG&index=3&pp=gAQBiAQB8AUB"]
destination = r'C:\users\Trahald\Desktop'

from pytube import YouTube
import os

for link in videosLinks:
    try:
        yt = YouTube(link)
        # Print status in cyan
        print(yt.title, "\033[96m {}\033[00m".format("in progess"))
        video = yt.streams.filter(only_audio=True).first()
        outFile = video.download(output_path=destination)
        # Change file extension
        base, extension = os.path.splitext(outFile)
        newFile = base + '.mp3'
        os.rename(outFile, newFile)
        # Print status in green
        print(yt.title, "\033[92m {}\033[00m".format("finished"))
    except Exception as error:
        # Print status in red
        print("\033[91m {}\033[00m".format("An error occured:"), error)
        continue
