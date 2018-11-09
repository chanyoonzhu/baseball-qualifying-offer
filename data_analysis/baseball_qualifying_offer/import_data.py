import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://questionnaire-148920.appspot.com/swe/data.html'

def fetch_html(url):
    # parse page
    html_page = urlopen(url)
    html = BeautifulSoup(html_page, "html.parser")
    return html

def fetch_salaries(html):
    return [tag.getText() for tag in html.findAll('td', {'class': 'player-salary'})]

def parse_salaries(salary_list):
    salaries = []
    for salary_raw in salary_list:
        try: 
            salaries.append(parse_int(salary_raw))
        except:
            pass
    return salaries

def parse_int(str):
    num_str = re.sub(r'\D', '', str)
    num = int(num_str)
    return num

