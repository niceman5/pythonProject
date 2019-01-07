'''
정규표현식을 처리하는 모듈 re
'''

import  re

# re.search(pattern, sting, flags)
# 지정문 문자열이 해당 정규 표현식에 일치하는지 확인
# pattern : 정규표현식
# sting : 정규표현식에 일치하는지 확인할 문자열
# flags : 정규 표현식을 컴파일 할때 동작을 변경하는 플래그를 지정
# 반환값 : 잋치하면 해당 객체를 반환한다. 일치하지 않으면 None

# re.match(pattern, sting, flags)
# 지정된 문자열이 정규 표현식에 일치하는지 확인. search()와 다르게 문자열의 맨 앞글자에서 부터 확인

