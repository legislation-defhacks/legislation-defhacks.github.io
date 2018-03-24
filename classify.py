import json
import requests

r = requests.get('https://api.propublica.org/congress/v1/members/A000360/votes.json')
print(r)
