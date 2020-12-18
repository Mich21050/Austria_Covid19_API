import getStats
from flask import Flask, request
from flask_restful import Api,Resource,reqparse
import threading
from datetime import datetime
import time


class TestThreading(object):
    secs = 5
    def __init__(self, interval=secs):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            x = datetime.today()
            y = x.replace(day=x.day+1, hour = 14, minute=30,second=0,microsecond=0)
            delta_t = y-x
            self.interval = delta_t.seconds+1
            print("ran loop", datetime.now())
            getStats.init()
            alBl = getStats.allBl()
            alGm = getStats.allGm()
            time.sleep(self.interval)

app = Flask(__name__)
getStats.init()
global alBl
global alGm
global alStat
alBl = getStats.allBl()
alGm = getStats.allGm()
alStat = getStats.allStat()
for x in range(len(alBl)):
    if alBl[x]["Bundesland"] == "Österreich":
        print(alBl[x]["fallSum"])
        print(alBl[x]["geheiltSum"])
tr = TestThreading()

for el in alStat:
    print(el["Bundesland"])
    print(el["testGesamt"])


@app.route("/api/v1/cases", methods=['GET'])
def cases():
    blLand = request.args.get('bundesland')
    Gm = request.args.get('bezirk')
    if(blLand is not None):
        for el in alBl:
            if(blLand.lower() == el["Bundesland"].lower()):
                return el,200
    for x in alGm:
        if(Gm.lower() == x["Bezirk"].lower()):
            return x,200
    return "Not found",404

@app.route("/api/v1/stats", methods=['GET'])
def stats():
    blLand = request.args.get('bundesland')
    if(blLand is not None):
        for el in alStat:
            if(blLand.lower() == el["Bundesland"].lower()):
                return el,200
    return "Not found",404

app.run(debug=True)