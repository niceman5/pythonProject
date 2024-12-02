from collections import defaultdict

# lambda표현식을 key후크로 넘겨 리스트를 길이로 정렬한다.
names = ['Scoewwww','aaaaaa','bvvv','CCCC']
names.sort(key=lambda x: len(x))
print(names)

# key를 찾을수 없을때마다 로그를 남기고 0을 리턴
def log_missing():
    print('Key added!!')
    return 0

current = {'green':12, 'blue':3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
print(current, type(current))
print(increments, type(increments), type(increments[0]))

# defultdict은 딕셔너리를 만드는 dict의 서브클래스

result = defaultdict(log_missing, current)
print('before', dict(result))
for key, amount in increments:
    result[key] += amount
print('After', dict(result))    

