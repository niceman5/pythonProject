'''
문자열 관련 기능 테스트
'''

# isalnum 문자열이 숫자와 문자일때만 True
str1 = 'abc11'
str2 = 'anc##'
print(str1, 'isalnum=', str1.isalnum(), ' ', str2, 'isalnum=', str2.isalnum())

# isalpha 문자열이 문자열일때만 True, 한국어등 ascii문자열이 아니라 하더라도 숫자나 기호가 없으면 True
str1 = '가나aa'
str2 = 'anc##'
str3 = 'anc12'
print(str1, 'isalpha=', str1.isalpha(), ' ', str2, 'isalpha=', str3.isalpha(),' ', str3, 'isalpha=', str2.isalpha())

# isdecimal 문자열이 십진수일때만 True
str1 = '12344'
str2 = '1234a'
print(str1, 'isdecimal=', str1.isdecimal(), ' ', str2, 'isdecimal=', str2.isdecimal())

# isdecimal 문자열이 숫자일때만 True
str1 = '12344'
str2 = '1234a'
print(str1, 'isdigit=', str1.isdigit(), ' ', str2, 'isdigit=', str2.isdigit())

# isidentifier 식별자로 사용할수 있는 문자면 True, 변수로 사용 가능한지...
str1 = 'a122'
str2 = '0Print'
print(str1, 'isidentifier=', str1.isidentifier(), ' ', str2, 'isidentifier=', str2.isidentifier())

# islower 문자열이 모두 소문자이면 True
str1 = 'a12ba2'
str2 = '0Print'
print(str1, 'islower=', str1.islower(), ' ', str2, 'islower=', str2.islower())

# isupper 문자열이 모두 대문자 True
str1 = 'a12ba2'
str2 = '0PRINT'
print(str1, 'isupper=', str1.isupper(), ' ', str2, 'isupper=', str2.isupper())

# isspace 스페이스, 탭이면 True
str1 = ' '
str2 = 'b'
print(str1, 'isspace=', str1.isspace(), ' ', str2, 'isspace=', str2.isspace())

# isnumeric 문자열이 숫자일때만 True
str1 = '12344'
str2 = '1234a'
print(str1, 'isnumeric=', str1.isnumeric(), ' ', str2, 'isnumeric=', str2.isnumeric())

# isprintable 출력가눙한 문자면 True
str1 = ' '
str2 = 'b'
print(str1, 'isprintable=', str1.isprintable(), ' ', str2, 'isprintable=', str2.isprintable())


print()
'''
문자열 반환 메서드
'''
str1 = 'HELLO world'
print(str1,  ' ', 'upper=', str1.upper())       #대문자로
print(str1,  ' ', 'lower=', str1.lower())       #소문자로
print(str1,  ' ', 'swapcase=', str1.swapcase()) #대문자 -> 소문자, 소문자는 대문자로
print(str1,  ' ', 'capitalize=', str1.capitalize()) #처음문자는 대문자 나머지는 소문자
print(str1,  ' ', 'title=', str1.title())       #단어마다 대문자+소문자로 변경
print(str1,  ' ', 'replace=', str1.replace('L', '*', 1))       #치환
print(str1,  ' ', 'replace=', str1.replace('L', '*'))       #치환
print(str1,  ' ', 'replace=', str1.replace('HELLO', '가나다'))       #치환


print()
'''
서식지정
'''
print('{} is better than {}'.format('아름다운', '가나다라'))
print('{1} is better than {0}'.format('아름다운', '가나다라'))
print('my name is {name}'.format(name='가나다라'))

person = {'name':'가나다라', 'email':'aaa@aaa.com'}
print('My email address={email}'.format_map(person))

'''
복잡한 서식 지정
'''
word = ['spam', 'ham', 'eggds']
print('I like {0[2]}'.format(word))
person = {'name':'가나다라', 'email':'aaa@aaa.com'}
print('My name is {person[name]}'.format(person=person))

from datetime import datetime
now = datetime.now()
print('Today is {0.year}-{0.month}-{0.day}'.format(now))
print(now)


'''
포멧 지정
'''
import math
print('|{:<30}|'.format('left align'))          # 왼쪽 정렬
print('|{:->30}|'.format('right align'))        # 오른쪽 정렬 빈자리애ㅔ '-'
print('|{:*^30}|'.format('center align'))       # 중앙 정렬
print('{0:b} {0:o}, {0:d} {0:x} {0:X}'.format(1000))    #각 진수로 표시
print('{0} {0:f}'.format(math.pi))              # 고정 소수점 문자열로 변환
print('{:%}'.format(0.045))                     # 백분율료 표시
print('{:,}'.format(1000000))                     # 세자리마다 , 4.2표시 앞자리는 전체 자리수, 뒤는 소수점
print('{:4.2f} {:2.2%}'.format(math.pi, 0.045))
now = datetime.now()
print('Today {:%y-%m-%d %H:%M:%S}'.format(now))     #날짜 형식
print('Today {:%Y-%m-%d %H:%M:%S}'.format(now))


'''
기타문자열 메서드
'''
print('Python Best Best'.find('Be'))
print('Python Best Best'.find('Be', 9))     #9번째 이후부터 count
print('Python Best Best'.split())           #리스트로 반환
print('Python| Best| Best'.split(sep='|'))           #리스트로 반환
image_suffix = ('jpg','png','gif')
print('image.gif'.endswith(image_suffix))   #지정된 접미사를 가진 문자열을 검색.suffix는 튜플로 지정, start, end는 조사할 위치
print('image.spl'.endswith(image_suffix))

'''
문자열 상수를 이용할수 있음
'''
import string
print('a' in string.ascii_lowercase)        # 소문자인지
print('a' in string.ascii_uppercase)        # 대문자인지
print('a' in string.ascii_letters)          # 영문자 전체
print('a' in string.punctuation)            # 기호문자인지 []()등
print('[' in string.punctuation)
#string.whitespace      공백으로 취급받는 문자열....탭이나 엔터등
