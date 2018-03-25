import json
import requests

import numpy as np
from sklearn import linear_model, datasets

payload = {'X-API-Key': 'FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9'}
request = requests.get('https://api.propublica.org/congress/v1/members/K000388/votes.json', headers=payload)
jsonParse = request.json()

billsAndVotes = jsonParse["results"][0]["votes"]

X = []
Y = []
for bill in billsAndVotes:
    data = []
    data.append(bill["total"]["yes"])
    data.append(bill["total"]["no"])
    # data.append(bill["total"][])
    Y.append(bill["position"])
    print(bill["bill"]["bill_id"])
    # print(bill["position"])
    X.append(data)

logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X, Y)
Z = []
logreg.predict(Z)
