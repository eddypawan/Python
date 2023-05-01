import webbrowser
import random

# Define the YouTube video link
link = "https://www.youtube.com/watch?v"

# Loop through 10 times
for i in range(2):
    # Generate a random start time between 0 and the video duration - 40 seconds
    duration = 180  # Set the video duration in seconds
    start_time = random.randint(0, duration - 40)

    # Open the video link with the start time and duration parameters
    params = {"t": f"{start_time}s", "end": f"{start_time+random.randint(10,40)}s"}
    url = link + "?" + "&".join([f"{k}={v}" for k, v in params.items()])
    webbrowser.open(url)
