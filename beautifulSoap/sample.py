import requests
from bs4 import BeautifulSoup

# replace the URL below with the one you want to extract text from
url = 'https://www.jkrishnamurti.org/content/alpino-italy-4th-public-talk-9th-july-1933'

# make a request to the website and get its HTML content
response = requests.get(url)
html_content = response.content

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# extract the text from the webpage
#text = soup.get_text()

# Find the first p tag with text "Krishnamurti Texts"
krishna_p_tag = soup.find('p', text='Krishnamurti Texts')

# Find all p tags before the krishna_p_tag
before_krishna_p_tags = krishna_p_tag.find_all_previous('p')

# Print the text content of each p tag
for p_tag in reversed(before_krishna_p_tags):
    print(p_tag.get_text())
