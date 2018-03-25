import json
import requests
import os
import numpy as np
from sklearn import linear_model, datasets


def trainPersonClassifier(person):
    bills = []
    personvotes = []
    years = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]
    for year in years:
        path = 'data/votes/' + year + '/'
        for folder in os.listdir(path):
            filename = path + str(folder) + '/data.json'
            json_data = json.load(open(filename))
            if 'bill' in json_data:
                if json_data["chamber"] == 'h':
                    bill = []
                    # print(filename)
                    bill.append(hash(json_data["bill"]["type"]))
                    bill.append(hash(json_data["category"]))
                    bill.append(hash(json_data["requires"]))
                    bill.append(hash(json_data["type"]))
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
                    if vote != None:
                        bills.append(bill)
                        personvotes.append(vote)
                    else:
                        break

    # print(len(bills))
    # print(len(personvotes))

    bill_len = len(bills)
    vote_len = len(personvotes)

    trainbills = bills[:bill_len-100]
    testbills = bills[-100:]
    trainvotes = personvotes[:bill_len-100]
    test_ans = personvotes[-100:]

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
    return accuracy

trainPersonClassifier("Jayapal")
