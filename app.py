import json
from data_analysis.main import *
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")

def hello():
    return render_template('index.html')

@app.route("/fetch")

def fetch():
    data = fetch_data()

    callback = request.args.get('callback')
    return '{0}({1})'.format(callback, data)



if __name__ == "__main__":
    app.run()