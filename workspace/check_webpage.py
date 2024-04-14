# filename: check_webpage.py
import urllib.request

def check_webpage(url):
    response = urllib.request.urlopen(url)
    the_page = response.read()

    return the_page

url = "https://www.example.com"
content = check_webpage(url)
print("Content of webpage:")
print(content)