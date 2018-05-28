##
#  list에서 가장 긴 sring을 찾는 방식
# 
names = ['Cecilia','Lisa','Maria']
letters = [len(n) for n in names]

long_name = ''
max_letter = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letter:
        long_name = names[i]
        max_letter = count

print('--------------------------------------')
print(long_name)        
print(max_letter)

long_name = ''
max_letter = 0

for name, count in zip(names, letters):
    if count > max_letter:
        long_name = name
        max_letter = count

print(long_name)        
print(max_letter)        

# zip사용시 주의할점
# 메모리를 많이 사용함으로 매우 큰 이터레이터를 사용할때는 내장모둘 itertools에 있는 izip을 사용할 것
# 입력 이터레이터들이 길이가 틀리면 zip이 이상하게 동작한다.
# zip은 감깐 이터레이터가 끝날때 까지 튜플을 계속 넘긴다. 이터레이터가 같으면 잘 동작
# zip으로 실해할 리스트의 길이가 같다고 확신하지 못하면 내장모둘 itertools 의 zip_longest를 사용 권고



