import zlib
text = '한국어 테스트'
b = text.encode('utf-8')
print(len(b))
c_data = zlib.compress(b)
print(len(c_data))

# 압축할 데이터가 작으면 압축한 결과가 더 클수있음

long_text = b'A'*100000
print(len(long_text))
c_data = zlib.compress(long_text)
print(len(c_data))
uc_data = zlib.decompress(c_data)
print(len(uc_data))

import gzip
with gzip.open('c:\\00.dev\\Study\\Python\\00.LibExample\\sample.gz','wt') as f:
    f.write('한국어 텍스트를 gzip으로 압축하기')
    f.write('A'*10000)		    
# 압축 파일이 생성됨

with gzip.open('c:\\00.dev\\Study\\Python\\00.LibExample\\sample.gz','rt') as f:
    content = f.read()
print(len(content))
# 압축을 열어서 평문으로 읽음.
# text 압축 gzip.compress() gzip.decompress()

