#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Lookup phone numbers on who-called.co.uk
from bs4 import BeautifulSoup
import requests

def whoCalled(number, includeComments=False):
    """Supply a phone number and get a result back indicating 'spam'
    level of the number. Oprtion includeComments boolean parameter to
    return first page of comments."""
    try:
        r = requests.get("https://who-called.co.uk/Number/" + number)
        if r.status_code != 200:
            return {"status" : "Error", "Reason" : "Bad server response"}
        if "Oops! Could not Find it" in r.text:
            return {"status" : "Error", "Reason" : "Malformed number"}
        soup = BeautifulSoup(r.text, 'html.parser')
    except Exception, e:
        return {"status" : "Error", "Reason" : str(e)}

    #Attempt to get the 'type' of number
    numType = "Unknown"
    try:
        t = soup.find("div", {"class" : "titleSecRow"}).findAll("div")[3].text
        if "Type:" in t:
            numType = t[6:]
    except Exception, e:
        pass

    try:
        d = soup.find("div", {"class" : "numberDetails"})
        tc = [i.text.replace(":","") for i in  d.findAll("div", {"class": "textColumn"})]
        dc = [i.text for i in  d.findAll("div", {"class": "dataColumn"})]
        result = dict(zip(tc,dc))
        result["Number"] = number
        result["Number type"] = numType
    except Exception, e:
        return {"status" : "Error", "Reason" : str(e)}

    #Comments - just the first page
    if includeComments:
        if soup.find("h2", {"class" : "numberRanks"}):
            try:
                numComments = soup.find("h2", {"class" : "numberRanks"}).text.replace("COMMENTS: ","").strip()
                #comments = []
                cc = soup.find("table", {"class" : "numberTable"})
                comments = [i.text for i in cc.findAll("p", {"class" : "numberDescShort"})]
                result["Comments"] = comments
            except:
                pass

    return result

if __name__ == "__main__":
    import sys
    from pprint import pprint as pp
    if len(sys.argv) < 2:
        print "Error: Please supply phone number as command line argument (supply second argument 'c' to get comments)"
        exit(-1)
    if len(sys.argv) == 3 and sys.argv[2] == "c":
        pp(whoCalled(sys.argv[1], True))
    else:
        pp(whoCalled(sys.argv[1], False))
