
# 파일을 비교하고 결과출력
# diff

import difflib
import sys

with open('file01.py', 'r') as hosts0:
    with open('file01.py.bak', 'r') as hosts1:
        diff = difflib.unified_diff(
            hosts0.readlines(),
            hosts1.readlines(),
            fromfile='hosts0',
            tofile='hosts1',
            n=0,
        )
        for line in diff:
            print(line, end='')