import requests
import random
import time

link = "https://www.youtube.com/watch?v="
proxies = [
    "http://181.111.178.74:8999",
    "http://190.19.114.104:8080",
    "http://177.55.207.38:8080"
]

# Define headers to mimic a real user
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Define a function to mimic a real user watching the video
def watch_video():
    # Make the initial request to the video link
    response = requests.get(link, headers=headers)
    time.sleep(10)

    # Generate a random start time and make a request with the start time parameter
    duration = 180
    start_time = random.randint(0, duration - 40)
    params = {"t": f"{start_time}s"}
    response = requests.get(link, headers=headers, proxies={"http": random.choice(proxies)}, params=params)
    time.sleep(5)

    # Scroll down the page
    scroll_distance = random.randint(500, 1000)
    requests.get(link, headers=headers, proxies={"http": random.choice(proxies)}, params={"scroll": "by", "value": f"{scroll_distance}"})
    time.sleep(5)

    # Scroll up the page
    requests.get(link, headers=headers, proxies={"http": random.choice(proxies)}, params={"scroll": "by", "value": "-100"})
    time.sleep(5)

    # Generate a random skip time and make a request with the start time and end time parameters
    skip_time = random.randint(start_time + 10, duration - 10)
    params = {"t": f"{start_time}s", "end": f"{skip_time}s"}
    response = requests.get(link, headers=headers, proxies={"http": random.choice(proxies)}, params=params)
    time.sleep(5)

    # Make a request with the end time parameter to simulate watching the entire video
    params = {"t": f"{duration}s", "end": f"{duration+10}s"}
    response = requests.get(link, headers=headers, proxies={"http": random.choice(proxies)}, params=params)
    time.sleep(5)

# Call the watch_video function multiple times to mimic multiple users watching the video
for i in range(10):
    watch_video()
