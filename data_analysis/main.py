import json
from .baseball_qualifying_offer.import_data import *

def fetch_data():

    data = {}

    html = fetch_html(url)
    # get table
    table = fetch_table(html)
    # calculate offer
    salaries= [i for i in table[1]][1:]
    offer = calc_qualifying_offer(salaries)

    data['table'] = table
    data['offer'] = offer
    data['year'] = YEAR
    data['level'] = LEVEL
    
    return json.dumps(data)
 
if __name__ == "__main__":
    fetch_data()