import heapq

data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]

h = []  # 힙 생성
for score in data:
    heapq.heappush(h, score)  # 힙에 데이터 저장

print(h, type(h))    

for i in range(3):
    print(heapq.heappop(h))  # 최솟값부터 힙 반환
    
    
# heapq.nsmallest(n, iterable)는 반복 가능한 객체(iterable) 데이터 집합에서 n개의 
# 가장 작은 요소로 구성된 리스트를 반환한다.
# 꼴찌부터 순위를 매긴다면 heapq.nlargest(3, data)를 사용하면 된다.
print(heapq.nsmallest(3, data))    