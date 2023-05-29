"""리스트를 반환하는 대신 제너레이터를 고려해야 함
"""

# 리스트를 직접반환 하는 코드임
# 모든 결과를 리스트에 저장했다 리턴. 대량의 처리시 메모리 사용이 클수 있음
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


# 리스트로 반환하는 부분이 없어 훨씬 쉬운 코드
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = "서울시 영등포구 당산동 sk v1빌딩 1004호"
result = index_words(address)
print(result)

result1 = list(index_words_iter(address))
print(result1)

result2 = list(index_words_iter(address))
print(result1)