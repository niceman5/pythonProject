# s = "133303"
# answer = []
# for i in s:
#     print(answer[-1:])
#     if answer[-1:] == [i]:
#         continue
#     answer.append(i)
#
# print(answer)
#
# lst=[1,3,4]
# print(lst[-1:])

# s = "abcde"
# print(s[2:3])


import collections

lst1 = ['a','b','c','a','f','g']
tup1 = ['b','d','e','e','f','f','g','h']

c1 = collections.Counter(lst1)
c2 = collections.Counter(tup1)

# 합집합
print(c1+c2)                    
print(list((c1+c2).elements()))

# 교집합
print(c1&c2)
print(list((c1&c2).elements()))

# 차집합
print(c1-c2)
print(list((c1-c2).elements()))

# 최대값
print(c1|c2)
print(list((c1|c2).elements()))