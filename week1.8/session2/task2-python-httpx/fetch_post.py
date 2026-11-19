"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

if (str(response).find("404") > -1):
    print("Error: Failed to GET " + url + ".")
else:
    print(response.json())      # response object, json() method
