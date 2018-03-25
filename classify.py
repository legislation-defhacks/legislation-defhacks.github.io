import json
import requests
import os
import numpy as np
from sklearn import linear_model, datasets

# payload = {'X-API-Key': 'FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9'}
# request = requests.get('https://api.propublica.org/congress/v1/members/K000388/votes.json', headers=payload)
# jsonParse = request.json()
person = "Jayapal"
bills = []
path = 'data/votes/2017/'
personvotes = []
for folder in os.listdir(path):
    filename = path + str(folder) + '/data.json'
    json_data = json.load(open(filename))
    if 'bill' in json_data:
        if json_data["chamber"] == 'h':
            bill = []
            print(filename)
            bill.append(hash(json_data["bill"]["type"]))
            bill.append(hash(json_data["category"]))
            bill.append(hash(json_data["requires"]))
            bill.append(hash(json_data["type"]))
            bills.append(bill)
            # print(bill)
            # search for person in the votes
            votes = json_data["votes"]
            # yes votes (aye, yea, and yes)
            aye = []
            if "Aye" in votes:
                aye = votes["Aye"]
            elif "Yea" in votes:
                aye = votes["Yea"]
            else:
                aye = votes["Yes"]
            # no votes:
            nay = []
            if "Nay" in votes:
                nay = votes["Nay"]
            else:
                nay = votes["No"]
            # not voting and present
            notvoting = votes["Not Voting"]
            present = votes["Present"]
            vote = None
            for a in aye:
                if a["display_name"] == person:
                    vote = "Aye"
            for n in nay:
                if n["display_name"] == person:
                    vote = "Nay"
            for nv in notvoting:
                if nv["display_name"] == person:
                    vote = "Not Voting"
            for p in present:
                if p["display_name"] == person:
                    vote = "Present"
            personvotes.append(vote)


X = np.array(bills)
Y = np.array(personvotes)

logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X, Y)
# logreg.predict(Z)
