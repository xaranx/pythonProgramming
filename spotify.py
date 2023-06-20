import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

res = requests.get("https://api.spotify.com/v1/me/shows?offset=0&limit=20")

print(json.dumps(res.json(), indent=2))