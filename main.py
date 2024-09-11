import os
import shutil

from pytube import YouTube

## Download video
filename = "./Videos"

print("Which Youtube video should be downloaded?")
URL = input('URL: ')
video = YouTube(URL)

if os.path.exists(f"{filename}/{video.title}.mp4"):
    print("Video already downloaded")
    exit()

try:
    video.streams.get_highest_resolution().download()
except ValueError:
    print(f"Cannot download this video: {URL}")

## Create folder
if not os.path.exists(filename):
    os.makedirs(filename, exist_ok=True)

if os.path.exists(f"{video.title}.mp4"):
    shutil.move(f"{video.title}.mp4", filename)
    print(f"{video.title}.mp4 is moved to \"{filename}\"")

print(video.metadata)
