from bs4  import BeautifulSoup
from urllib import request
from urllib import parse

# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

# base64방식
parse_quote = parse.quote('고양이')

print(parse_quote)

img_url = url+parse_quote   # 서버에 요청할 url완성

savePath = 'D:\\PythonProject\\Project\\day20190518\\img\\'

try:
    os.makedirs(savePath)
except:
    print('Create Directory Fail!!!!')

html = request.urlopen(img_url).read()
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
list = soup.find_all('img', class_='_img')   # image tag중에 class속성이 _img것들

# print(list[0:])
# print(len(list))

# for img in list:
#     # print(type(img))
#     print(img['data-source'])
for idx, img in enumerate(list, 1):
    # print(img['data-source'])
    savename = savePath + str(idx) + '.png'
    request.urlretrieve(img['data-source'], savename)

print('success!!')
