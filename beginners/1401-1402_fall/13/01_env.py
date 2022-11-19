# 2.7
# print "Hello"

# 3
print("Hello")

# venv
# python -m venv venv

import requests

response = requests.get("https://digikala.com")
# print(response.json())
print(response.status_code)
print(response.text)

# pip freeze > requirements.txt 
# pip install -r .\requirements.txt