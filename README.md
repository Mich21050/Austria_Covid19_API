# Austria Covid19 API
Just a small python api after I discovered the data source of the Austrian COVID19 Dashboard

# Introduction
After getting bored from being stuck at home for a few months now I started to poke around the offical Austrian COVID19 Dashboard and I found something really interesting. Turns out that all the raw data is just passed as a json file (and a really nice one). So I wrote a small API in python using flask. The api is getting its data from the offical raw data.

# Endpoint/Variables
Currently the api only has 2 endpoints.
* the cases endpoint; supports both ?bundesland and ?bezirk (more on that later)
* the stats endpoint; only supports ?bundesland; The stats endpoint it esentially the same as the cases just with a few more statistiscs.

As mentioned above, the api only has 2 "options" but I think they are pretty self explanatory.

# Usage of the cases endpoint
If you only need some basic numbers I would recommend the cases endpoint. Just make a simple GET request passing the designated area like so:

**Request:**
```
GET http://127.0.0.1:5000/api/v1/cases?bundesland=niederösterreich
```
or
```
GET http://127.0.0.1:5000/api/v1/stats?bezirk=baden
```
**Example Response:**
```
{
"Bundesland": "Niederösterreich",
"Time": "2020-12-17T00:00:00",
"aktiveSum": 11514,
"fallSum": 49057,
"geheiltSum": 36825,
"siebenTageInzidenz": 173.42650035296836,
"totSum": 718
}
```
I think all the values are pretty self explanatory.

# Usage of the stats enpoint
Should you need more data the stats endpoint would be better:

**Request:**
```
GET http://127.0.0.1:5000/api/v1/stats?bundesland=niederösterreich
```
**Example Response:**
```
{
  "Bundesland": "Nieder\u00f6sterreich", 
  "Time": "2020-12-17T00:00:00", 
  "aktiveSum": 11514, 
  "fallSum": 49057, 
  "geheiltSum": 36825, 
  "hospFree": 669, 
  "hospital": 351, 
  "icu": 82, 
  "icuFree": 111, 
  "siebenTageInzidenz": 173.42650035296836, 
  "testGesamt": 623657, 
  "totSum": 718
}
```
I think those values are also pretty self explanatory.

# Final Word
I hope this helps some people developing their own applications. If you have any quetsions please dont hesitate to contact me. :)

# TODO
* Code cleanup
* better readme
* small bug fixes
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:cc="http://creativecommons.org/ns#" class="license-text"><a rel="cc:attributionURL" property="dct:title" href="https://github.com/Mich21050/Austria_Covid19_Api/">Austria COVID19 API</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Mich21050/">Michael Wanninger</a> is licensed under <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" /></a></p>
