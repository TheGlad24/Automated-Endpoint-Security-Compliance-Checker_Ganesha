# Flask app to view reports
# Save as dashboard.py

from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("compliance_report_win.json") as f:
        win = json.load(f)
    with open("compliance_report_macos.json") as f:
        mac = json.load(f)
    return render_template("index.html", win=win, mac=mac)

#@app.route("/api/windows")
#def api_windows():
   #return jsonify(json.load(open("compliance_report_win.json")))

@app.route("/api/macos")
def api_macos():
    return jsonify(json.load(open("compliance_report_macos.json")))

if __name__ == "__main__":
    app.run(debug=True)
