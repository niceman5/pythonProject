import textwrap

# 함수는 매개변수 width로 전달한 길이만큼 문자열을 줄여 표시한다. 글 1문자를 길이 2가 아닌 1로 계산한다는 점에 조심하자.
# 뒤에 나오는 문자 [...]을 포함해서 15글자
print(textwrap.shorten("Life is too short, you need python", width=15))

# 축약 표시 [...]을 ...으로 변경하고 싶다면 다음처럼 매개변수 placeholder를 이용한다.
print(textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15, placeholder='...'))

# 다음 문자열(long_text)은 너무 길어 읽기가 불편하므로 적당한 길이로 줄 바꿈할때 단어 단위로 잘른다.
long_text = 'Life is too short, you need python. ' * 10
print(long_text)
# width 길이만큼 자르고 이를 리스트로 만들어 반환한다.
result = textwrap.wrap(long_text, width=70)
print(result)
print('\n'.join(result))

# textwrap.fill() 함수를 사용하면 이 과정을 한 번으로 줄일 수 있다.
print(textwrap.fill(long_text, width=70))