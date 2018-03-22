# WhoCalled API
Small wrapper to query data from https://who-called.co.uk.

## Command line usage:
Supply the number as the first command line argument, and optional 'c' character as the second command line option to include comments.
```
➜  WhoCalledAPI python who.py 07537182429
{u'Average rate': u'Harassing',
 u'Last checked': u'a few seconds ago ',
 'Number': '07537182429',
 u'Number of searches': u'30613',
 'Number type': u'Mobiles'}
 ```

 ## API Wrapper usage:
 Run the service direct from the command line:
 ```
 ➜  WhoCalledAPI python __init__.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

 Or preferably integrate with your webserver: http://flask.pocoo.org/docs/0.12/deploying/

The endpoint is ```/number/<number>``` with an optional parameter of ```comments=true```.
```
➜  WhoCalledAPI curl http://localhost:5000/number/07537182429
{
  "Average rate": "Harassing",
  "Last checked": "a few seconds ago ",
  "Number": "07537182429",
  "Number of searches": "30620",
  "Number type": "Mobiles"
}
```
```
➜  WhoCalledAPI curl http://localhost:5000/number/07537182429\?comments\=true
{
  "Average rate": "Harassing",
  "Comments": [
    "If they any caller cant be bothered to show their company name I wont answer.",
    "don't pick up its a waste of time",
    "Wankers",
    "Said he was not trying to sell me anything and it was just a survey. I hung up & blocked them",
    "I only answered it as it was a normal looking mobile number. An Asian guy asked if I was Mrs. **** and I said Are you calling from a call centre? Goodbye! and hung up.",
    "Salesman. Asked if I was Mr Watkins. When I told him I was homeless and had no money he hung up.",
    "When i asked them to remove my number they asked me for it?",
    "Rude Asian woman. Leave me alone efffing professional pests",
    "I LOVE BLOCKING SCAM CALLERS",
    "garbled message.",
    "tel:07537182429 very annoying asian(?) guy, some kind of survey, i asked him how did he get my number, he ignored the question, he was insisting on confirming my name, number now blocked",
    "I just rang them back and it had an automated message which said \u201cThanks for calling I love my offers\u201d\nBlocked this number, unsure how the managed to get my number in first place.",
    "Scammers, asian or not... normal companies don't use a mobile number to cold call people......",
    "Scammers hang up don't waste your time",
    "They phoned twice but I did not recognise no. I tried calling back but got garbled message so have blocked it",
    "Answered this because it flashed up uk and looked like a mobile. Voice mail message about some survey or something. Blocked number.",
    "Didn't pick up but glad that I didn't after seeing this. Incidentally, what's with all the hate towards Asians? Are some of the natives that backwards?",
    "Sick of getting number calling. Blocked",
    "I didn't recognise the number to my mobile so did not answer.",
    "voice mail"
  ],
  "Last checked": "a few seconds ago ",
  "Number": "07537182429",
  "Number of searches": "30621",
  "Number type": "Mobiles"
}
```
