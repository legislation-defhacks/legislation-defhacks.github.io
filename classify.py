import json
import requests

payload = {'X-API-Key': 'FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9'}
r = requests.get('https://api.propublica.org/congress/v1/members/A000360/votes.json', headers=payload)
# r.json()
print(r.json())
