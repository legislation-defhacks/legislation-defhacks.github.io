import json
import requests
import os


import numpy as np
from sklearn import linear_model, datasets

payload = {'X-API-Key': 'FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9'}
# request = requests.get('https://api.propublica.org/congress/v1/members/K000388/votes.json', headers=payload)
# jsonParse = request.json()

bills = []
path = 'data/votes/2017/'

for folder in os.listdir(path):
    filename = path + str(folder) + '/data.json'
    json_data = json.load(open(filename))
    if 'bill' in json_data:
        if json_data["chamber"] == 'h':
            bill = []
            bill.append(json_data["bill"]["type"])
            bill.append(json_data["category"])
            bill.append(json_data["requires"])
            bill.append(json_data["type"])
            print(bill)
            bills.append(bill)






# X = []
# Y = []
# for bill in billsAndVotes:
#     data = []
#     data.append(bill["total"]["yes"])
#     data.append(bill["total"]["no"])
#     # data.append(bill["total"][])
#     Y.append(bill["position"])
#     print(bill["bill"]["bill_id"])
#     # print(bill["position"])
#     X.append(data)
#
# logreg = linear_model.LogisticRegression(C=1e5)
# logreg.fit(X, Y)
# Z = []
# logreg.predict(Z)
