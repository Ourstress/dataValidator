from flask import Flask
from goodtables import validate
import csv
import requests

CSV_URL = "http://www.stat.umn.edu/geyer/3701/data/p3p3.csv"

with requests.get(CSV_URL, stream=True) as r:
	lines = (line.decode('utf-8') for line in r.iter_lines())
	csvData = ""
	for row in csv.reader(lines):
		csvData = csvData + str(row)

report = validate(lines)

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>hello world</h1><p>report has table count of {report['table-count'] }</p><p>{csvData}</p>"

@app.route("/hello.html")
def hey():
	return "<h1>Boo!</h1>"


if __name__ == "__main__":
	app.run(debug=True)