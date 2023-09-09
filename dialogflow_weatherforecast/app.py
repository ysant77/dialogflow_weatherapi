from flask import Flask, Response, request
import json

from util import *

app = Flask(__name__)


def getPriceIntentHandler(countryname):
    countryname = "".join( countryname.split() )
    weather = getWeather(countryname)
    return f"The weather of {countryname} is {weather}"

@app.route("/", methods = ["POST"])
def main():
    
    req = request.get_json(silent=True, force=True)
    print(req)
    intent_name = req["queryResult"]["intent"]["displayName"]
    
    if intent_name == "getWeatherInfo":
        countryname = req["queryResult"]["parameters"]["geo-country"]
        resp_text = getPriceIntentHandler(countryname)
        
    else:
        resp_text = "Unable to find a matching intent. Try again."

    resp = {
        "fulfillmentText": resp_text
    }

    return Response(json.dumps(resp), status=200, content_type="application/json")

app.run(host='0.0.0.0', port=60000, debug=True)
#ngrok http https://localhost:5000 -host-header="localhost:5000"






