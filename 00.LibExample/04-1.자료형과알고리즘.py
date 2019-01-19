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