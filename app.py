from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>hello world</h1><p>Hello hello there</p>"

@app.route("/hello.html")
def hey():
	return "<h1>Boo!</h1>"


if __name__ == "__main__":
	app.run(debug=True)