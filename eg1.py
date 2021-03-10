# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:02:15 2021

@author: sravan
"""

from flask import Flask,jsonify,request

app = Flask(__name__)

stores = [
    {
     'name':'mahaLakshmi',
     'items':
         [
             {
                 'name':'pappu',
                 'price':50
             }
         ]
     }
]

@app.route("/store",methods=['POST'])
def createStore():
    store = request.get_json()
    new_store = {'name':store['name'],'items':[]}
    stores.append(new_store)
    return "Successfully created"

@app.route("/store")
def getAllStore():
    return jsonify({'stores':stores})

@app.route("/store/<string:name>")
def getStore(name):
    for store in stores:
        if name==store['name']:
            return store
    return "No Such Store Exists"

@app.route("/store/<string:name>/items")
def getAllItems(name):
    for store in stores:
        if name==store['name']:
            return jsonify({'items':store['items']})
    return "No Such Store Exists"

@app.route("/store/<string:name>",methods=['POST'])
def addItems(name):
    item = request.get_json()
    for store in stores:
        if name==store['name']:
            store['items'].append({'name':item['name'],'price':item['price']})
            return "successfully Appended"
    return "No Such Store Exists"

#app.run(host='192.168.29.181',port=12345)







