from collections import Counter
import re
def checkio(text: str) -> str:
    reStr = ''
    # 소문자로 골라내고 영문자만.
    text = re.findall(r"[a-z]", text.lower())
    # print(text)
    # 문자열에 ' '을 삽입해서 분리.....문자수를 Count
    d = dict(Counter(' '.join(text).split(' ')))
    lst = list(d.items())
    lst.sort(key = lambda data : data[1])
    value = lst[len(lst)-1]
    # print(value)
    lst = [ v for v in lst if v[1] == value[1] ]
    lst.sort(key=lambda data: data[0])
    reStr = lst[0][0]

    # print('text=',text)
    # print('reStr=', reStr)
    return reStr

# import string
#
# def checkio(text):
#     """
#     We iterate through latyn alphabet and count each letter in the text.
#     Then 'max' selects the most frequent letter.
#     For the case when we have several equal letter,
#     'max' selects the first from they.
#     """
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)

# from collections import Counter
#
# def checkio(text):
#     count = Counter([x for x in text.lower() if x.isalpha()])
#     m = max(count.values())
#     return sorted([x for (x, y) in count.items() if y == m])[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")