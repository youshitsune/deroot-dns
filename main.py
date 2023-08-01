from flask import Flask
from flask import request
import json

app = Flask(__name__)

domains = {"youshitsune.tech": "45.77.200.184"}

@app.route("/resolve", methods=["POST"])
def resolve():
    data = request.get_json()
    if data["domain"] in domains.keys():
        return {"ip": domains[data["domain"]]}
    else:
        return "404"
    

app.run()
