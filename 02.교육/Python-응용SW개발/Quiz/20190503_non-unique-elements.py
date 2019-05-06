# 비어 있지 않은 정수 (X) 목록이 제공됩니다. 이 태스크의 경우이 목록에있는 고유하지 않은 요소로만 구성된 목록을 리턴해야합니다.
# 이렇게하려면 모든 고유 요소 (주어진 목록에 한 번만 포함 된 요소)를 제거해야합니다. 이 작업을 해결할 때 목록의 순서를 변경하지
# 마십시오. 예 : [1, 2, 3, 1, 3] 1 및 3 개의 고유하지 않은 요소 및 결과는 [1, 3, 1, 3]입니다.
#
# Precondition:
# 0 < len(data) < 1000

#Your optional code here
#You can import some modules or create additional functions

from collections import Counter

def checkio(data: list) -> list:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.
    for key, values in dict(Counter(data)).items():
        if values == 1:
            data = [x for x in data if x != key]
    #replace this for solution
    return data


#  다른 풀이들....
# def checkio(arr):
#   return [x for x in arr if arr.count(x) > 1]

# def checkio(data):
#     counter = Counter(data)
#     return [item for item in data if counter[item] > 1]

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list





if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
