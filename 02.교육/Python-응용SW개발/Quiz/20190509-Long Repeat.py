# 이 임무는이 시리즈의 첫 번째 임무입니다. 여기서 동일한 문자로 구성된 가장 긴 하위 문자열의 길이를 찾아야합니다. 예를 들어,
# "aaabbcaaaa"행에는 "aaa", "bb", "c"및 "aaaa"와 같은 4 개의 하위 문자열이 있습니다. 마지막 부분 문자열은 대답을 만드는
# 가장 긴 부분 문자열입니다.


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

