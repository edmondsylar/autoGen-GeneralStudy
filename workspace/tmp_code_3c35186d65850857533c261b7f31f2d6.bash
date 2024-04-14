python3 -c "$(cat << EOF
import requests
def check_webpage(url):
    response = requests.get(url)
    return response.content
url = 'https://www.example.com'
content = check_webpage(url)
print('Content of webpage:')
print(content)
EOF
)"