from urllib import parse

result = parse.urlparse('https://docs.python.org/ko/3/library/urllib.html?q=example')
print(1, result, type(result))
print(2, result.geturl())
print(3, result.scheme)
print(4, result[0], result[2], result[3])
print(5, result.hostname, result.query)
# query결과를 dict형으로 받는다.
print(6, parse.parse_qs(result.query))
# 하나의 키에 값이 여러개도 확인 가능
print(7, parse.parse_qs('key=1&key=2'))
# key1은 값이 없음으로 생략됨 keep_blank_values=True면 값이 없으면 빈 문자로 처리된다.
print(8, parse.parse_qs('key1=&key2=2'))
print(9, parse.parse_qs('key1=&key2=2', keep_blank_values=True))
# 쿼리문자열 조합하기.....순서는 보장되지 않음. dict형태나 튜플이 올수있음
print(10, parse.urlencode({'key1':1, 'key2':2, 'key3':'abbbb'}))
print(11, parse.urlencode([('key1',1),('key2',2),('key3','파이썬')]))

q = {'key1':1, 'key2': ['aaaa','bbbb'], 'key3':'abbbb'}
print(12, parse.urlencode(q)) # ['aaaa','bbbb']를 문자열로 변환
print(13, parse.urlencode(q, doseq=True)) #하나의 키에 여러값이 전달됨

from urllib import request
# GET method이용
res = request.urlopen('http://httpbin.org/get')
print(20, res.code)
print(21, res.read())
# 매개변수를 붙여서 이용하기
res = request.urlopen('http://httpbin.org/get?key1=value1')
print(22, res.code)
print(23, res.read())
# 사용자정의 헤더 설정
headers = {'Accept':'application/json'}
req = request.Request('http://httpbin.org/get', headers=headers)
print(24, req, type(req))



# post방식으로 요청하기
data = 'key1=value1&key2=value2'
res = request.urlopen('http://httpbin.org/post', data=data.encode())
print(25, res.code)
# 한번 읽고 나면 다시 못읽음...
urltxt = res.read()
print(26, urltxt)
# bytes를 str로 변경한다.
txt = urltxt.decode('utf-8')
print(txt, type(txt))


#get/post이외의 방식으로 요청
req = request.Request('http://httpbin.org/', method='HEAD')
res = request.urlopen(req)
print(30, res.code)
print(31, res.read())