import json
import requests

payload = {'X-API-Key': 'FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9'}
request = requests.get('https://api.propublica.org/congress/v1/members/K000388/votes.json', headers=payload)
jsonParse = request.json()

billsAndVotes = jsonParse["results"][0]["votes"]

# memberData = []
for bill in billsAndVotes:
    print(bill["bill"]["bill_id"])
# print()
