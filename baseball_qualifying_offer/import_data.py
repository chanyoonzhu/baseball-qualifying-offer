from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://questionnaire-148920.appspot.com/swe/data.html'

def fetch_html(url):

    # parse page
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")

    s = soup.findAll('td')
    
    return s

print(fetch_html(url))