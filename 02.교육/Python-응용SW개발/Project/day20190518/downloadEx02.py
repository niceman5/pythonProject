import urllib.request as req

imgUrl = 'http://blogfiles.naver.net/20140417_20/wnsgud4648_1397736892888TiSDU_PNG/%B0%ED%BE%E7%C0%CC.PNG'

savePath = 'D:\\PythonProject\\Project\\day20190518\\cat02_01.jpg'

img =  req.urlopen(imgUrl).read()

# print(img)
saveImg = open(savePath, 'wb')
saveImg.write(img)
saveImg.close()

print('success~~~'')
