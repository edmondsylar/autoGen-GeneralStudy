# filename: information_gathering.py

import datetime
import platform
import requests

# Get current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Check operating system
print("Operating System:", platform.system())

# Print content of a webpage
response = requests.get('https://www.example.com')
print("Status code:", response.status_code)
print("Content of the webpage:")
print(response.content.decode())