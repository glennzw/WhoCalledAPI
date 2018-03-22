#!/usr/bin/python
# -*- coding: utf-8 -*-
# JSON API to query spaminess of phone number
# e.g: /number/07537182429
#      /number/07537182429?comments=true
from flask import Flask, jsonify, request
from who import *

app = Flask(__name__)

@app.route('/number/<number>')
def checkNumber(number):
    comments = False
    print request.args.get('comments')
    if request.args.get('comments') and request.args.get('comments').lower() == "true":
        comments = True
    result = whoCalled(number, comments)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False)
