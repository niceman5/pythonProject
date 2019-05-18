# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


list_test = ['하나','둘','셋','넷']

path = 'D:\\PythonProject\\Project\\day20190518\\new_file.txt'
try:
    f = open(path, 'x') # exists 파일이 존재하면 오류
except:
    print('This file is already exists.')
else:
    for i, v in enumerate(list_test):
        print(i+1, v)
        # f.write(str(i+1)+'. '+v+'\n')
        f.write('{}. {}\n'.format(i+1, v))
    f.close()
finally:
    print('success')
