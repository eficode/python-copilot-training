from flask import Flask, render_template, request, redirect, url_for
import csv
from io import StringIO
import pandas as pd

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
        df = pd.DataFrame(uploaded_data)
        sort_by = request.args.get('sort_by')
        order = request.args.get('order', 'asc')

        if sort_by and sort_by in df.columns:
            df = df.sort_values(by=sort_by, ascending=(order == 'asc'))

        table_html = df.to_html(classes='table table-striped', index=False, border=0)
        sortable_header = '<tr>' + ''.join(
            f'<th><a href="?sort_by={col}&order={"desc" if sort_by == col and order == "asc" else "asc"}">{col} '
            f'{"▲" if sort_by == col and order == "asc" else "▼" if sort_by == col and order == "desc" else ""}</a></th>'
            for col in df.columns
        ) + '</tr>'
        sortable_table_html = table_html.replace(
            '<thead>' + table_html.split('<thead>')[1].split('</thead>')[0] + '</thead>',
            f'<thead>{sortable_header}</thead>'
        )
        return render_template('data.html', title=csv_title, data=sortable_table_html)
    except NameError:
        return "No data uploaded yet"

if __name__ == '__main__':
    app.run(debug=True, port=4999)
