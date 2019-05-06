# 주어진 iterable을 정렬하여 요소가 감소하는 빈도 순서로 끝나도록합니다. 즉 요소에 나타나는 횟수입니다. 두 요소의 빈도가 같으면
# iterable의 첫 번째 모양과 동일한 순서로 끝나야합니다

from collections import Counter

def frequency_sort(items):
    # your code here
    lst = []
    items = list(dict(Counter(items)).items())
    items.sort(key=lambda data: data[1], reverse=True)

    for key, value in items:
        print(key, value)
        for j in range(0, value):
            lst.append(key)
    # print(lst)
    return lst


# def frequency_sort(items):
#     return sorted(items, key=lambda e: (-items.count(e), items.index(e)))

# def frequency_sort(items):
#     # your code here
#     counter = collections.Counter(items)
#     array = []
#     append = array.append
#     for v, c in counter.most_common():
#         for i in range(c):
#             append(v)
#     return array

if __name__ == '__main__':
    print("Example:")
    # print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort([4,6,2,2,2,6,4,4,4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
