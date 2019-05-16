# 이 임무는이 시리즈의 첫 번째 임무입니다. 여기서 동일한 문자로 구성된 가장 긴 하위 문자열의 길이를 찾아야합니다. 예를 들어,
# "aaabbcaaaa"행에는 "aaa", "bb", "c"및 "aaaa"와 같은 4 개의 하위 문자열이 있습니다. 마지막 부분 문자열은 대답을 만드는
# 가장 긴 부분 문자열입니다.


def long_repeat(line):
    max_char = ''
    tmp_char = ''


    for v in line:
        if len(tmp_char) > 0 and tmp_char[-1] != v:
            if len(tmp_char) > len(max_char):
                max_char = tmp_char
            tmp_char = ''
        tmp_char = tmp_char + v
    # print(tmp_char,max_char)
    if len(max_char) == 0:
        max_char = tmp_char

    return len(max_char)



from itertools import groupby

# def long_repeat(line):
#     return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)
#


# def long_repeat(line):
#     m = 0
#     p = 0
#     for x in range(len(line)):
#         if x < len(line) - 1:
#             if line[x] == line[x + 1]:
#                 p += 1
#             else:
#                 p = 0
#         if p + 1 > m:
#             m = p + 1
#
#     # your code here
#     return m

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert long_repeat('sdsffffse') == 4, "First"
    # assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    # assert long_repeat('abababaab') == 2, "Third"
    # assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, "2"
    print('"Run" is good. How is "Check"?')

