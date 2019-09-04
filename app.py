from bottle import route, run, get, post, request
import pandas as pd 

@route('/')
def index():
    return "Hello!"

@get('/csv') 
def csv():
    return '''
        <form action="/csv" method="post" enctype="multipart/form-data">
            <input name="data" type="file" accept=".csv" />
            <input value="check csv file" type="submit" />
        </form>
    '''

@post('/csv')
def do_csv():
    if request.files.get('data'):
        dataFile = request.files.get('data')
        data = pd.read_csv(dataFile.file, index_col=0)
        return f"""
        <p>File name: {dataFile.filename}</p>
        <p>File name: {data.head()}</p>
        """
    else:
        return "<p>Login failed.</p>"

run(host='localhost', port=8080, debug=True)