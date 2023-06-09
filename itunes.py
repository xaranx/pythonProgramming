# https://itunes.apple.com/search?entity=song&limit&term=
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#print(json.dumps(response.json(), indent=2))

o = response.json()

for result in o["results"]:
    trackName = (result["trackName"])
    print(trackName)

    file = open("track.txt", "a")
    file.write(f"{trackName}\n")
    file.close()
