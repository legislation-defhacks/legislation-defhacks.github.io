import json
import requests
import os
import numpy as np
from sklearn import linear_model, datasets

import urllib
import csv
from flask import Flask
from flask import request
from flask_cors import CORS
import json

import os, sys, csv, urllib

app = Flask(__name__)
CORS(app)

def newHash(str):
    res = 0
    for word in str.split(" "):
        for c in word:
            res += hash(c)
    return res

tb1 = [hash("hr"), hash("passage"), hash("1/2"), newHash("Crime, Terrorism, Homeland Security, and Investigations."), newHash("To repeal the Gun-Free School Zones Act of 1990 and amendments to that Act.")]
tb2 = [hash("hr"), hash("passage"), hash("1/2"), newHash("Natural Resources; Ways and Means"), newHash("To amend and enhance the High Seas Driftnet Fishing Moratorium Protection Act to improve the conservation of sharks.")]
tb3 = [hash("hr"), hash("passage"), hash("1/2"), newHash("Education and the Workforce"), newHash("To address the needs of individuals with disabilities within the Jeanne Clery Disclosure of Campus Security Policy and Campus Crime Statistics Act.")]

def trainPersonClassifier(person, billnum):
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
                    print(filename)
                    bill.append(hash(json_data["bill"]["type"]))
                    bill.append(hash(json_data["category"]))
                    bill.append(hash(json_data["requires"]))
                    bill.append(newHash(json_data["type"]))
                    if "question" in json_data:
                        bill.append(newHash(json_data["question"]))
                    else:
                        bill.append(newHash(json_data["subject"]))


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

    Z = np.array([tb1, tb2, tb3])
    b1 = logreg.predict(Z)
    print(b1)

    return accuracy, b1[billnum]

trainPersonClassifier("Pelosi", 0)

@app.route("/spectrum" , methods=['GET', 'POST'])
def spectrum():
    # urlList = request.form['urlArray']
    #
    # urlList = json.loads(urlList)
    # print(urlList, "FIRST ONE")
    # print urlList

    # numberOfArticles = len(urlList) + 2
    # #print numberOfArticles
    # conservativeScore = 1
    # liberalScore = 1
    # for url in urlList:
    #     try:
    #         actualURL = url.split("/")[2]
    #     except:
    #         print url, "error!!"
    #     # actualURL = url.split("/")[2]
    #     if "www." in actualURL:
    #         actualURL = actualURL.split("www.")[1]
    #     else:
    #         continue
    #     with open('data_liberal.csv', 'r') as f:
    #         for line in f.read().split('\r'):
    #             if actualURL == line:
    #                 liberalScore += 1
    #     with open('data_conservative.csv', 'r') as f:
    #         for line in f.read().split('\r'):
    #             if actualURL == line:
    #                 conservativeScore += 1
    #
    # #print conservativeScore
    # conservativeScore = float(conservativeScore)/float(numberOfArticles)
    # liberalScore = float(liberalScore)/float(numberOfArticles)
    # #print conservativeScore
    # #print liberalScore
    # val = 0
    # if liberalScore > conservativeScore:
    #     val =  -liberalScore*100
    # elif conservativeScore > liberalScore:
    #     val =  conservativeScore*100
    # else:
    #     val =  0
    # print "FINALLLL VALUEEEEE", str(val)
    # return str(val)

    return "88"
app.run()
