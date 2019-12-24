import requests
from bs4 import BeautifulSoup

URL = 'https://finance.yahoo.com/quote/BTC-EUR/'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find_all('div', {'class':'D(ib) Mend(20px)'})[0].find('span').text

print(title + ' Euros')
