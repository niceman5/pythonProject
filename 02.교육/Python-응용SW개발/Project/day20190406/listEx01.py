value = [2,4,6,8,'hi~~',[1,3,5], 2.5]
print(type(value))
print(value)
print('첫번째:', value[0])
print('네번째:', value[3])

# 이어진값 구하기...2,3번 슬라이싱은 끝값은 제외됨...+1한걸로 해야 함
print(value[1:3])
print('마지막:', value[-1])
print('마지막데이터 자료형:', type(value[-1]))

print(value[-2])
print(value[-2][1])
print('문자열요소출력1:', value[-3])
print('문자열요소출력2:', value[-3][1])
