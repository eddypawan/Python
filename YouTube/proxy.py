import requests
import random

# Define the YouTube video link
link = "https://www.youtube.com/watch?v="

# Define a list of proxy servers
proxies = [
     "http://181.111.178.74:8999",	
    "http://190.19.114.104:8080",
    "http://177.55.207.38:8080"
]

# Loop through 10 times
for i in range(10):
    # Generate a random start time between 0 and the video duration - 40 seconds
    duration = 180  # Set the video duration in seconds
    start_time = random.randint(0, duration - 40)

    # Choose a random proxy server from the list
    proxy = {"http": random.choice(proxies)}

    # Make the request using the chosen proxy server
    params = {"t": f"{start_time}s", "end": f"{start_time+random.randint(10,40)}s"}
    response = requests.get(link, proxies=proxy, params=params)

    print(response)
    # Print the response status code
    print(response.status_code)
