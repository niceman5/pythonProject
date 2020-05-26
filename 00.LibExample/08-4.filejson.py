import json
from decimal import Decimal

data = [{'id':123, 'entities':{'url':'python.org','hashtag':['#python', '#pythonworker']}, 'name':'김태훈' }]
# print(data, type(data))
# json형태로 만듬
# print(json.dumps(data, indent=2))
# json형태로 인코딩한다.
jtxt = json.dumps(data, indent=2, sort_keys=True)
print(jtxt, type(jtxt))

json_str = '["ham", 1.0, {"a":false, "b":null}]'
jtxt2 = json.loads(json_str)
print(jtxt2, type(jtxt2))
# json에 포함된 부동 소수점의 취급을 지정
jtxt2 = json.loads(json_str, parse_float=Decimal)
print(jtxt2, type(jtxt2))

# jtxt2 = json.loads(json_str, parse_int=int)
# print(jtxt2, type(jtxt2))
# json이 list형식임으로 node추가 방법
data[0]['entities']['hashtag'].append('#pyhack')
jtxt = json.dumps(data, indent=2, sort_keys=True)
print(jtxt, type(jtxt))