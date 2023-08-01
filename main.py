from flask import Flask
from flask import request
import json

app = Flask(__name__)

domains = {"youshitsune.tech": "45.77.200.184"}

@app.route("/", methods=["GET"])
def index():
    return "Welcome to my dns server"
@app.route("/resolve", methods=["POST"])
def resolve():
    data = request.get_json()
    if data["domain"] in domains.keys():
        return {"ip": domains[data["domain"]]}
    else:
        return "404"
    

app.run(port=5353)
