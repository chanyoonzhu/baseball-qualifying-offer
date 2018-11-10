import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from .calculate_offer import *

url = 'https://questionnaire-148920.appspot.com/swe/data.html'
YEAR = '2016'
LEVEL = 'MLB'
RANGE = 125

def fetch_html(url):
    # parse page
    html_page = urlopen(url)
    html = BeautifulSoup(html_page, "html.parser")
    return html

def fetch_table(html):
    result = []
    table = html.find('table')
    result += fetch_table_head(table)
    result += fetch_table_body(table)
    return result

def fetch_table_head(table):
    result = []
    head = table.find('thead')
    result.append([])
    allcols = head.findAll('th')
    result[0].append(allcols[0].getText())
    result[0].append(allcols[1].getText())
    return result

def fetch_table_body(table):
    result = []
    rows = table.find('tbody').findAll('tr')
    for row in rows:
        rowData = []
        allcols = row.findAll('td')
        legitimateData = True
        for col in allcols:
            if col['class'][0] == 'player-salary':
                try: 
                    rowData.append(parse_int(col.getText()))
                except:
                    legitimateData = False
            elif col['class'][0] == 'player-name':
                rowData.append(col.getText())
            # data validation
            if (col['class'][0] == 'player-year' and col.getText() != YEAR or 
                col['class'][0] == 'player-level' and col.getText() != LEVEL):
                    legitimateData = False
        if legitimateData:
            result.append(rowData) 
    return result

def fetch_best(table):
    return best_to_range(table, RANGE)

def fetch_qualifying_offer(table):
    amount = calc_qualifying_offer(table, RANGE)
    return format_currency(amount)

def parse_int(str):
    num_str = re.sub(r'\D', '', str)
    num = int(num_str)
    return num

def format_currency(val):
    return '${:,}'.format(val)