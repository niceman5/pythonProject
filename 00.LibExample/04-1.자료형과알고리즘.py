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

# deque 큐의 맨 앞과 맨 끝에서 추가와 삭제를 등록된 데이터 수와 상관없이 일정한 속도로 수행
print('{:->100}'.format(''))
deq = collections.deque('spam')
print(deq, ' 인덱스로 접근 deq[1]=', deq[1])
deq[1] = 'P'
print(deq, ' 인덱스로 접근 deq[1]=', deq[1])

deq = collections.deque(maxlen=5)       # deq의 최대 길이 지정
for v in range(10):
    deq.append(v)
    if len(deq) >= 5:
        print(list(deq), sum(deq)/5)

deq = collections.deque('12345')
print(deq)
deq.rotate(3)
print('rotate(3)=', deq)
deq.rotate(-3)
print('rotate(-3)=', deq)
# deque객체의 첫 요소와 두번째 요소 변경
deq = collections.deque('12345')
print(deq)
first = deq.popleft()
deq.rotate(-1)
deq.appendleft(first)
deq.rotate(1)
print(deq)

import heapq
# heapq이용하면 일련의 값으로 부터 최소값을 빠르게 구한다.
print('{:->100}'.format(''))
queue = []
heapq.heappush(queue, 2)
heapq.heappush(queue, 0)
heapq.heappush(queue, 1)
print('queue=', queue)
print('heappop=', heapq.heappop(queue), queue)
print('heappop=', heapq.heappop(queue), queue)
print('heappop=', heapq.heappop(queue), queue)      # 최소값부터 삭제된다.

queue=[1,2,3,4,5]
print('queue=', queue)
heapq.heapify(queue)            # 리스트객체의 heap요소를 정령하여 heapq로 삼는다.
heapq.heappushpop(queue, 6)     # 리스트객체 heap에 item을 추가하고 최소값을 삭제하고 해당 값을 리턴한다. 선삽입 후삭제
print('queue=', queue)          # heapreplace()는 석삭제 후삽입처리\...
heapq.heappushpop(queue, 7)
print('queue=', queue)