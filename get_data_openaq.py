import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://api.openaq.org/v1/cities")
jprint(response.json())
params = {
    'city': 'Los Angeles',
    'parameter': 'o3'
}
response = requests.get("https://api.openaq.org/v1/measurements", params=params)
jprint(response.json())
