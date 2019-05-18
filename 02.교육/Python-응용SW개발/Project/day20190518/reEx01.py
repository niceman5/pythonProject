#1. re모듈 import
import re

data = 'abc. d2y mart food m day 379'

#2. compile(정규표현식)
# p = re.compile('[abc]')
# p = re.compile('[m]')
# p = re.compile('[a-zA-Z]')  # 모든 알파벳을 찾아라.
# p = re.compile('[0-9]')  # 모든 숫자
# p = re.compile('[135]') # 13룰 찾아
# p = re.compile('[^135]')    # 135를 제외한 모든것
# p = re.compile('[\d]')  # 숫자와 매치 [0-9]와 동일
# p = re.compile('[\D]')  # 숫자가 아닌것과 매치 [^0-9]와 동일
# p = re.compile('day')   # 단어로 찾음
# p = re.compile('d.y')   # .은 아무거나 적용됨 d로시작 아무거사 y로 종료
# p = re.compile('fo*d')
# p = re.compile('fo{2}d')
p = re.compile('[a-z]+')    # [a-z]까자 한개이상 반복된것


#3. 검색함수
# print('math :', p.match(data))  # math는 첫번째부터 찾음. m이면 None
m = p.match(data)
print(m)
print('group :', m.group())
print('start :', m.start())
print('end :', m.end())
print('span :', m.span())

# print('search :', p.search(data))   # data전체에서 찾음
# print('findall :', p.findall(data))
# print('finditer :', p.finditer(data))
#
# for v in p.finditer(data):
#     print(v)
