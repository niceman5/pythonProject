# 데이터의 횟수세기는 collections.Counter를 사용하면 편리
# Counter는 사전형에서 파생된 클래스로 사전에 데이터건수를 카운트하는 기능이 추가
import collections
c = collections.Counter()
c['spam'] += 1
c[100] += 2
c[200] += 3
c[300] += 4
c['spam'] += 2
print(c)
print('{:->100}'.format(''))

# counter
counter = collections.Counter([1,2,3,4,1,2,5,6,7,3,2])
print(counter)
print('{:->100}'.format(''))
counter1 = collections.Counter(spam=1, ham=2)
counter2 = collections.Counter(ham=3, egg=4)
print('counter1=', counter1, ' counter2=', counter2)
print('Counter합=', counter1+counter2)
print('Counter차=', counter1-counter2)
print('Counter 교집합=', counter1&counter2)
print('Counter OR=', counter1|counter2) #키값이 같으면 두 값중 큰쪽의 값을 사용
counter1 += counter2    # 좌변의 counter요소에 우변의 counter요소를 더한다.
print(counter1)
print('{:->100}'.format(''))

# ChainMap
d1 = {'spam':1, 'ham':100}
d2 = {'ham':200}
c = collections.ChainMap(d1, d2)    # 여러개의 사전을 묶오 각각의 사전 요소를 하나의 사전으로 검색할수 있게 한다.
print(c['spam'], c['ham'])          # 객체 요소를 추가또는 삭제하면 맨 앞에 등록한 매핑객체에 반영됨
c['bacom'] = 10
print(d1)
c.clear()       # d1이 clear됨.
print(d1)

# defaultdict 없는 값 참조시 오류나는데 defaultdict사용하면 오류 안나고 기본값이 리턴된다.
print('{:->100}'.format(''))
def ret_value():
    return 'return default value'
d = collections.defaultdict(ret_value, spam=100)
print('기존값=', d['spam'])        #
print('없는값=', d['aaa'])

# OrderedDict
# 일반적으로 객체에 저장한 값을 읽어올때 반복해서 읽으면 순서가 틀릴수 있음. 이 class사용하면 등록한 순서대로 객체를 가져온다.

# namedtuple 데이터를 그룹으로 관리할때 사용. 3차원 좌표등을 튜플로 보관, namedtuple은 정수 인덱스 뿐만 아니라 속성, 이름지정하여 요소 취
# 득
print('{:->100}'.format(''))
c = collections.namedtuple('Coor', 'X,Y,Z')
c1 = c(100,-100, 50)
print('c1=', c1)
print(c1.X)
