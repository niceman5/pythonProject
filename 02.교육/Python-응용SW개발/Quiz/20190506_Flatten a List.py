# 모든 정수 값을 하나의 단순 목록에 넣어야합니다. 순서는 왼쪽에서 오른쪽으로의 문자열 표현을 사용하여 원래 목록에
# 있었던 순서와 같아야합니다. 우리는이 프로그램을 작고 쉽게 숨겨서 Nikola에서 숨길 필요가 있습니다. 이 때문에 코드는 공백이있는 140
# 자보다 짧아야합니다.

# Input data: A nested list with integers.
#
# Output data: The one-dimensional list with integers.
#
# Example:
#
# flat_list([1, 2, 3]) == [1, 2, 3]
# flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
# flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
# flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]

def flat_list(array):
    lst = []
    for v in array:
        if isinstance(v, list):
            for v1 in flat_list(v):
                lst.append(v1)
        else:
            lst.append(v)

    return lst

# def flat_list(array):
#     ret_list = []
#     for e in array:
#         if type(e) == list:
#             tmp_list = flat_list(e)
#             ret_list.extend(tmp_list)
#         else:
#             ret_list.append(e)
#     return ret_list


# def flat_list(array):
#     res = []
#     for i in array:
#         res.extend(flat_list(i) if isinstance(i, list) else [i])
#     return res


# def flat_list(l):
#     r = []
#     def f(l):
#         for i in l:
#             r.append(i) if type(i) is int else f(i)
#     f(l)
#     return r

if __name__ == '__main__':

    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')