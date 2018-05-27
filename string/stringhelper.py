# str이나 bytes를 입력받고 str을 반환
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value  # str 인스턴스


# str이나 bytes를 받고 bytes를 리턴
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str

    return value  # bytes 인스턴스


# s1 = b'가나다라'
print(to_str("가나다라"))

