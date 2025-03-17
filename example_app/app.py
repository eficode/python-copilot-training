from flask import Flask, render_template, request, redirect, url_for
import csv
from io import StringIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['csvFile']
        data = file.read().decode('utf-8')
        csv_data = csv.DictReader(StringIO(data))
        data = [row for row in csv_data]
        global uploaded_data
        global csv_title
        csv_title = file.filename
        uploaded_data = data

    return render_template('index.html')

@app.route('/data')
def data():
    try:
        return render_template('data.html', title=csv_title, data=uploaded_data)
    except NameError:
        return "No data uploaded yet"

if __name__ == '__main__':
    app.run(debug=True, port=4999)
