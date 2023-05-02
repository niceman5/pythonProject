##
#  list에서 가장 긴 string을 찾는 방식
# 
names = ['Cecilia', 'Lisa', 'Maria']
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
print(max_letter)

long_name = ''
max_letter = 0

for name, count in zip(names, letters):
    if count > max_letter:
        long_name = name
        max_letter = count

print(long_name)        
print(max_letter)        