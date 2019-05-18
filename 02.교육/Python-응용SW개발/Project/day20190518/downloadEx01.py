
# import urllib.request as ur
from urllib.request import urlretrieve

imgUrl = 'http://blogfiles.naver.net/20110521_64/wdr08100_1305961405269aUlsO_JPEG/%B1%CD%BF%A9%BF%EE_%B9%D9%C5%C1%C8%AD%B8%E9_%B0%ED%BE%E7%C0%CC_%B9%E8%B0%E6%C8%AD%B8%E9_1600x1200_297.jpg'

savePath = 'D:\\PythonProject\\Project\\day20190518\\cat03.jpg'

# ur.urlretrieve(imgUrl, savePath)
urlretrieve(imgUrl, savePath)

print('success!!!')
