import json
from .baseball_qualifying_offer.import_data import *

def fetch_data():

    data = {}

    html = fetch_html(url)
    # get table
    table = fetch_table(html)
    # get best
    best = fetch_best(table)
    # calculate offer
    offer = fetch_qualifying_offer(table)

    # assemble data
    data['table'] = table
    data['best'] = best
    data['offer'] = offer
    data['year'] = YEAR
    data['level'] = LEVEL
    
    return json.dumps(data)
 
if __name__ == "__main__":
    fetch_data()