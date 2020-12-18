import requests
import json
from datetime import datetime, time, timedelta

def init():
    cookies = {
        'lang': 'de',
        'area': '10',
        'BIGipServerpool_radw34': '335816970.20480.0000',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
        'Accept': '*/*',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Referer': 'https://covid19-dashboard.ages.at/dashboard.html',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    response = requests.get('https://covid19-dashboard.ages.at/data/JsonData.json', headers=headers, cookies=cookies)
    dataOut = open("out.json", "w")
    dataOut.write(json.dumps(json.loads(response.text), indent=2))
    dataOut.close()
    f = open("out.json")
    global dataload
    dataload = json.load(f)
    dataBl = dataload["CovidFaelle_Timeline"]
    global lsMid
    now = datetime.now()
    if now.time() < datetime(2020,12,1,15,0).time():
        tDelta = 2
    else:
        tDelta = 1
    lsMid = str(datetime.combine(datetime.today(), time.min) - timedelta(days=tDelta)).replace(" ","T")
    global tdStatsBl
    tdStatsBl = []
    for x in range(len(dataBl)):
        if(dataBl[x]["Time"] == lsMid):
            tdStatsBl.append(dataBl[x])

def allBl():
    datBl = [
        {
            "Bundesland": "Burgenland",
        },
        {
            "Bundesland": "Kärnten",
        },
        {
            "Bundesland": "Niederösterreich",
        },
        {
            "Bundesland": "Oberösterreich",
        },
        {
            "Bundesland": "Salzburg",
        },
        {
            "Bundesland": "Steiermark",
        },
        {
            "Bundesland": "Tirol",
        },
        {
            "Bundesland": "Vorarlberg",
        },
        {
            "Bundesland": "Wien",
        },
        {
            "Bundesland": "Österreich",
        }
    ]

    for x in range(len(datBl)):
        for y in range(len(tdStatsBl)):
            if datBl[x]["Bundesland"] == tdStatsBl[y]["Bundesland"]:
                datBl[x]["aktiveSum"] = tdStatsBl[y]["AnzahlFaelleSum"] - tdStatsBl[y]["AnzahlTotSum"] - tdStatsBl[y]["AnzahlGeheiltSum"]
                datBl[x]["Time"] = tdStatsBl[y]["Time"]
                datBl[x]["fallSum"] = tdStatsBl[y]["AnzahlFaelleSum"]
                datBl[x]["totSum"] = tdStatsBl[y]["AnzahlTotSum"]
                datBl[x]["geheiltSum"] = tdStatsBl[y]["AnzahlGeheiltSum"]
                datBl[x]["siebenTageInzidenz"] = tdStatsBl[y]["SiebenTageInzidenzFaelle"]
    return datBl

def allGm():
    dataGm = dataload["CovidFaelle_GKZ"]
    curTime = tdStatsBl[int(len(tdStatsBl)-1)]["Time"]
    for x in range(len(dataGm)):
        dataGm[x]["Time"] = curTime
    return dataGm

def allStat():
    datRaw = allBl()
    datAll = dataload["CovidFallzahlen"]
    moreStat = []
    for x in range(len(datAll)):
        if(datAll[x]["MeldeDatum"] == lsMid):
            moreStat.append(datAll[x])
    
    for x in range(len(datRaw)):
        for y in moreStat:
            if datRaw[x]["Bundesland"] == "Österreich":
                comp = "Alle"
            else:
                comp = datRaw[x]["Bundesland"]
            if(comp.lower() == y["Bundesland"].lower()):
                datRaw[x]["testGesamt"] = y["TestGesamt"]
                datRaw[x]["hospital"] = y["FZHosp"]
                datRaw[x]["icu"] = y["FZICU"]
                datRaw[x]["hospFree"] = y["FZHospFree"]
                datRaw[x]["icuFree"] = y["FZICUFree"]
    return datRaw
