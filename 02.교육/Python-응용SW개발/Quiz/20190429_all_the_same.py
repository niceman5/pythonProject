from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    bResult = True

    if len(elements) <= 1:
        return bResult
    var1 = elements[0]
    for val2 in elements[1:]:
        if var1 != val2:
            bResult = False
            break

    return bResult

# 다른 풀이들....
# def all_the_same(elements):
#    return elements[1:] == elements[:-1]
#
# def all_the_same(elements: List[Any]) -> bool:
#     return len(set(elements)) <= 1

# def all_the_same(elements):
#    return elements == elements[1:] + elements[:1]

# def all_the_same(elements):
#     el = iter(elements)
#     first = next(el, None)
#     return all(element == first for element in el)

if __name__ == '__main__':
    print("Example:")
    # print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert all_the_same([1, 1, 1]) == True
    # assert all_the_same([1, 2, 1]) == False
    # assert all_the_same(['a', 'a', 'a']) == True
    # assert all_the_same([]) == True
    # assert all_the_same([1]) == True
    print(all_the_same([10000, 99999]))
    print("Coding complete? Click 'Check' to earn cool rewards!")