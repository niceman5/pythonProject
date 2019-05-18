from bs4  import BeautifulSoup
import urllib.request as req

import sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'https://media.daum.net/'
savePath = 'D:\\PythonProject\\Project\\day20190518\\news.txt'

url_read = req.urlopen(url).read()
# print(url_read)
soup = BeautifulSoup(url_read, 'html.parser')
news = soup.find('ol', class_='list_popcmt').find_all('a')
# print(type(news))
for idx, v in enumerate(news, 1):
    print( '{}. {}'.format(idx, v.get_text().splitlines()[2].strip()))
