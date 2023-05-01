from pytube import YouTube
from moviepy.editor import VideoFileClip
import random

# Define the YouTube video link
link = "https://www.youtube.com/watch?v="

# Download the video
yt = YouTube(link)
stream = yt.streams.first()
filename = f"{yt.title}.mp4"
stream.download(filename=filename)

# Play the video 10 times with random start and end times
for i in range(10):
    duration = VideoFileClip(filename).duration
    start_time = random.uniform(0, duration - 40)
    end_time = start_time + random.uniform(10, 40)
    clip = VideoFileClip(filename).subclip(start_time, end_time)
    clip.preview()
