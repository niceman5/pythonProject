# 임시파일 처리

import tempfile
import os

# 임시파일 처리시 유니코드 처리를 해줘야 함. 안하면 오류
# NamedTemporaryFile(mode=’w+b’, buffering=None, encoding=None, newline=None, suffix=’’, prefix=’tmp’, dir=None, delete=True)
# TemporaryFile()과 정확히 동일한 역할을 합니다.
# 파일 시스템에서 볼 수 있는 파일이름을 반드시 갖도록 보장한다는 점에서 차이가 있습니다.
# 파일이름은 파일 객체의 name 속성에서 확인할 수 있습니다.
# delete=True 상태에서는 파일이 닫히는 동시에 삭제됩니다.
# file-like 객체는 일반 파일처럼 with 구문에서 이용할 수 있습니다.

with tempfile.NamedTemporaryFile() as tmp:
    tmp.write('가나다라 마바사아'.encode('utf-8'))
    tmp.seek(0)
    print(tmp.read().decode('utf-8'))
    fname = tmp.name
    print(fname)
    print(os.path.exists(fname))

tmp.close() # close하면 임시파일을 명시적으로 삭제한다.
print(os.path.exists(fname))


# fnmatch 파일명을 매칭시키는 기능....파일목록에서 특정 파일목록을 거르거나 할때 사용하면 될듯
# https://docs.python.org/ko/3/library/fnmatch.html

# glob - 특정 파일만 출력하기
# 현재 디렉토리에서 확장자가 jpg인 파일만 모아서 출력한다.
# 결과값이 list로....
import glob
for filename in glob.glob('c:\\00.dev\\Study\\Python\\00.LibExample\\*.py'):
    print(filename)



# 재귀적으로 현재 폴더의 모든 하위폴더까지 탐색하여 확장자가 jpg인 파일을 출력한다.

print('-'*50)
import glob
for filename in glob.iglob('**/*.jpg', recursive=True):
   print(filename)


# 에제) GuineaPig 폴더를 재귀적으로 돌며 jpg파일을 출력.
print('-'*50)
import glob
for filename in glob.iglob('c:\\00.dev\\Study\\Python\\**/*.jpg', recursive=True):
    print(filename)

# [] ? * 를 사용할수 있음/ escape문자를 만듬  --> 모르겠음
# print(glob.escape('c:\\00.dev\\Study\\Python\\00.LibExample\\06-[?]*.py') )


