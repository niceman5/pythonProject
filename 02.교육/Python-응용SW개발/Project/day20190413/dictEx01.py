a = { 'key':1234}
print(type(a), a)

# 하나의 데이터가 쌍으로 관리
# 키와 값이 하나의 데이터
# 저장순서를 유지하지 않음

dic = {'name':'kim', 'phone':'010-1111-1111'}
print(type(dic), dic)

print(dic['name'])      # index대신 key를 사용한다.
print(dic['phone'])

dic['addr'] = '강남'      # dic에 추가
print(dic)

##del dic['phone']      # 삭제
##print(dic)
dic['age'] = 20         # 숫자도 가능....
print(dic)

dic['name'] = '김'       # 이미 key가 있으면 update
print(dic)

keys = dic.keys()
print(type(keys), keys)
value = dic.values()
print(type(value), value)
print(dic.items())      #튜프로 받음
print(list(dic.items()))

print(type(dic.items()))
it = list(dic.items())  # 직접 값을 뽑을수가 없음...list변경해서 사용
print(it[0])

print(dic.get('name'))
print(dic.get('addr1', 'age'))  #없는 key면 다음값 isnull()비슷

key = list(dic.keys())
print(key[0])

print('name' in dic)        #True
print('addr2' in dic)       #False



