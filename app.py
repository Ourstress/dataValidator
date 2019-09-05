from flask import Flask, request
import requests
import pandas as pd 

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>hello world</h1><p>Hello hello there</p>"

@app.route('/csv', methods=['GET']) 
def csv():
    return '''
        <form action="/csv" method="post" enctype="multipart/form-data">
            <input name="data" type="file" accept=".csv" />
            <input value="check csv file" type="submit" />
        </form>
    '''

@app.route('/csv', methods=['POST'])
def do_csv():
    if request.files:
        dataFile = request.files['data']
        data = pd.read_csv(dataFile, index_col=0)
        return f"""
        <p>File name: {dataFile.filename}</p>
        <p>File name: {data.head()}</p>
        """
    else:
        return "<p>Login failed.</p>"

if __name__ == "__main__":
	app.run(debug=True) 