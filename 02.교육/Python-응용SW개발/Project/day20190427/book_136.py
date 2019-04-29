
a = [1,2,3,4]

##result = []
##for num in a:
##    result.append(num*3)
##print(result)    

# 이건 위의 코드를 한줄로...
##result = (num * 3 for num in a)
##print(result)
##print(type(result))
##for i in result:
##    print(i)

# 짝수인것만 만들어서 list로 만든다.,
##result = [num * 3 for num in a if num % 2 == 0]
##print(result)
##print(type(result))
##for i in result:
##    print(i)


#내포로 만들어지는 리스트도 중첩으로 만들수 있음.
result = [x*y for x in range(2,10)
                  for y in range(1,10)]
print(result)
                  
