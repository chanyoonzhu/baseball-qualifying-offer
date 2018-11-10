import json
from baseball_qualifying_offer.import_data import *
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")

def hello():
    data = fetch_data()
    return data

def fetch_data():

    data = {}

    html = fetch_html(url)
    salary_list = fetch_salaries(html)
    # get salary
    salaries = parse_salaries(salary_list)
    # get offer
    offer = calc_qualifying_offer(salaries)

    data['salary'] = salaries
    data['offer'] = offer

    callback = request.args.get('callback')
    return '{0}({1})'.format(callback, data)
    
    return json.dumps(data)
 
if __name__ == "__main__":
    app.run()