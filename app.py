from flask import Flask, request, render_template
import requests
import pandas as pd 
import PyPDF2
import io

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route('/csv', methods=['GET']) 
def csv():
    return '''
        <p>Validates CSV and PDF files</p>
        <form action="/csv" method="post" enctype="multipart/form-data">
            <input name="data" type="file" accept=".csv,.pdf" />
            <input value="check csv file" type="submit" />
        </form>
    '''

@app.route('/csv', methods=['POST'])
def do_csv():
    if request.files:
        dataFile = request.files['data']
        # Reading PDF https://stackoverflow.com/questions/55481813/how-to-read-pdf-from-in-memory-uploaded-file-python-3-6
        if dataFile.filename.endswith('.pdf'):
            data = PyPDF2.PdfFileReader(io.BytesIO(dataFile.read())).getPage(0)
        if dataFile.filename.endswith('.csv'):
            data = pd.read_csv(dataFile, index_col=0, header=None)
        return str(data)
        # return f"""
        # <p>File name: {dataFile.filename}</p>
        # {data.head().to_html()}
        # """
    else:
        return "<p>Login failed.</p>"

if __name__ == "__main__":
	app.run(debug=True) 