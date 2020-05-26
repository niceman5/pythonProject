import requests

r = requests.get('http://httpbin.org/get')
print(1, r)
print(2, r.text)

r = requests.get('http://httpbin.org/get', params='example')
print(3, r)
print(4, r.url)
print(5, r.text)

r = requests.get('http://httpbin.org/get', params={'key1':'value1'})
print(6, r)
print(7, r.url)
print(8, r.text)

headers = {'Accept':'application/json'}

r = requests.get('http://httpbin.org/get', params={'key1':'value1'}, headers=headers)
print(10, r)
print(11, r.url)
print(12, r.text)
print(13, r.json()) #응답을 json포맷으로 해석하고 사전으로 반환한다.
print(14, r.ok) # 응답코드가 정상이면 True아니면 False
print(15, r.status_code) #응답코드
print(16, r.headers) #사전 형식의 응답헤더
print(17, r.cookies) #응답에 포함된 쿠키정보를 지닌 객체

import base64
s = 'Python은 간단히 개발이 습득할수 있으며 이와 동시에 강략한 언어중 하나 입니다.'
# print(20, base64.b64encode(s))  -->문자열 전달하면 오류남\
print(20, base64.b64encode(s.encode()))
# 선택적 altchars는 +와 / 문자의 대체 알파벳을 지정하는 최소 길이 2(추가 문자는 무시됩니다)의
#  바이트열류 객체여야 합니다. 이를 통해 응용 프로그램은 URL이나 파일 시스템에서 안전한 Base64 
# 문자열을 생성할 수 있습니다. 기본값은 None이며, 표준 Base64 알파벳이 사용됩니다.
print(21, base64.b64encode(s.encode(), altchars=b'@*'))

#s = b'UHl0aG9u7J2AIOqwhOuLqO2eiCDqsJzrsJzsnbQg7Iq165Od7ZWg7IiYIOyeiOycvOupsCDsnbTsmYAg64@Z7Iuc7JeQIOqwleuete2VnCDslrjslrTspJEg7ZWY64KYIOyeheuLiOuLpC4='
s = b'UHl0aG9u7J2AIOqwhOuLqO2eiCDqsJzrsJzsnbQg7Iq165Od7ZWg7IiYIOyeiOycvOupsCDsnbTsmYAg64+Z7Iuc7JeQIOqwleuete2VnCDslrjslrTspJEg7ZWY64KYIOyeheuLiOuLpC4='
print(30, s, type(s))
print(31, base64.b64decode(s))
print(32, base64.b64decode(s).decode())

