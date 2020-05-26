import os
from pathlib import Path

# 파일시스템을 문자열이 아닌 객체로 다루게 되면서 얻게 된 큰 이익 중 하나는 연산자를 새롭게 정의할 수 있게 되었다는 점이다. 
# pathlib은 이것을 아주 아름답게 이용했다.

# https://docs.python.org/3/library/pathlib.html

dir1 = 'c:\\'
dir2 = '00.Dev'
dir3 = 'study'
dir4 = 'Python'
dir5 = '00.LibExample'
file1 = '00.String.py'

full1 = os.path.join(dir1,dir2,dir3,dir4,dir5,file1)
print(full1, os.path.exists(full1))

# 직관적으로 사용 가능함
full2 = Path(dir1) / dir2 / dir3 / dir4 / dir5 / file1
print(full2, os.path.exists(full2))

# Path.open()
from pathlib import Path

filename = '00.String.py'

# without pathlib
file = open(filename, 'r')

# with pathlib
path = Path(filename)
file = path.open('r')

# 파일 읽고 쓰기. 단 한 번의 I/O만 하면 된다면, 번거롭게 파일을 열고 닫을 필요 없이 사용할 수 있는 함수들이 있다.
# Path.write_text()
# Path.write_bytes()
# Path.read_text()
# Path.read_bytes()

from pathlib import Path

filename = full2._str
type(filename)
print('filename=' + filename)

# without pathlib
file = open(filename, 'r', encoding='utf-8')
r = file.read()
file.close()
# print(r)

# without pathlib2
with open(filename, 'r', encoding='utf-8') as f:
  r = f.read()
# print(r)

# with pathlib
p = Path(filename,encoding='utf-8')
r = p.read_text(encoding='utf-8')
print(r)





