import json
import requests
import os
import numpy as np
from sklearn import linear_model, datasets

# payload = {'X-API-Key': 'FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9'}
# request = requests.get('https://api.propublica.org/congress/v1/members/K000388/votes.json', headers=payload)
# jsonParse = request.json()
person = "Ryan (OH)"
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

trainbills = bills[:614]
testbills = bills[-50:]
trainvotes = personvotes[:614]
test_ans = personvotes[-50:]

X = np.array(trainbills)
Y = np.array(trainvotes)

logreg = linear_model.LogisticRegression()
logreg.fit(X, Y)
Z = np.array(testbills)

predictions = logreg.predict(Z)

accuracy = 0
for i in range(len(predictions)):
    if test_ans[i] == predictions[i]:
        accuracy += 1
print(accuracy)
