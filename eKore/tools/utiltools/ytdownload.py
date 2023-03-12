import os
import pytube
import time
from rich.progress import Progress
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop

P = '\033[35m' # pink
G1 = '\033[90m' # grey
w = '\033[37m' # white
P = '\033[35m' # purple
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
RE = '\033[0m' # reset
Y = '\033[33m' # yellow
B = '\033[34m' # blue
LG = '\033[37m' # lightgrey

def start():
    video_url = input(f"{C}> {w}Enter the YouTube video URL: ")

    youtube = pytube.YouTube(video_url)

    # IF PROBLEMS, COMMENT OUT THIS BELOW. FOR SOME REASON PYTUBE HAS PROBLEMS WITH GETTING .TITLE
    print(f"{C}> {w}Selected video: {youtube.title}")

    while True:
        file_format = input(f"{C}> {w}Enter the desired file format (MP3 or MP4): ")
        print("\033[F\033[K", end="")
        if file_format.lower() not in ['mp3', 'mp4']:
            print(f"{C}> {w}Invalid file format! Please enter either {R}MP3 {w}or {R}MP4{RE}.")
            time.sleep(1.5)
            print("\033[F\033[K", end="")
        else:
            break

    if file_format.lower() == 'mp3':
        stream = youtube.streams.filter(only_audio=True).first()
    else:
        stream = youtube.streams.get_highest_resolution()

    custom_file_name = input(f"{C}> {w}Enter a custom file name(or leave blank to use default): ")
    if custom_file_name:
        file_name = custom_file_name + '.' + file_format.lower()
    else:
        file_name = youtube.title + '.' + file_format.lower()

    with Progress() as progress:
        task1 = progress.add_task(stream.download(output_path=(os.path.join(os.path.dirname(__file__), '..', '..', 'output')), filename=file_name), total = 1000)
        print(f"{C}> {w}Downloading {file_format.upper()} file...")
        #stream.download(output_path=(os.path.join(os.path.dirname(__file__), '..', '..', 'output')), filename=file_name)
        while not progress.finished:
            progress.update(task1, advance=10)
            time.sleep(0.02)
    print(f"{C}> {w}File downloaded!")
    print(f"{C}> {w}Press '{R}Enter{w}' to exit.")
    input()

print(f"{C}> {w}Download complete!")

if __name__ == "__main__":
    start()