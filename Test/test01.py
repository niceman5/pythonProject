# lst1 = ['a','b','c','d','f','e']
# print(lst1)
# print(lst1[0:2])

lst = []
lst2 = []
for i in range(1, 50):
    lst.append(i)

print(lst)
lst2 = lst[0:20]
print(lst2)
del lst[:20]
print(lst)