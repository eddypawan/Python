import requests
import random

# proxy_list = ["123.45.67.89:8080", "234.56.78.90:8080", "345.67.89.01:8080"]
proxy_list = [
     "http://181.111.178.74:8999",	
    "http://190.19.114.104:8080",
    "http://177.55.207.38:8080"
]
video_url = "https://www.youtube.com/watch?v="

proxies = {
    'http': f'http://{random.choice(proxy_list)}',
    'https': f'http://{random.choice(proxy_list)}'
}

response = requests.get(video_url, proxies=proxies)
print(response.content)