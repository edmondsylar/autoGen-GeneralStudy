# filename: content_check.py

import requests

response = requests.get('https://www.example.com')
content = response.content.decode()

if "Example Domain" in content:
    print("The webpage contains the string 'Example Domain'.")
else:
    print("The webpage does not contain the string 'Example Domain'.")