import os.path
import time


file_nm = 'C:\\00.Dev\\Study\\Python\\00.LibExample\\00.String.py'
file_dir = 'C:\\00.Dev\\Study\\Python\\00.LibExample\\'
# 
print('파일경로 path의 절대 경로를 반환')
print(os.path.abspath('.'))
print(os.path.abspath('..'))

print('파일경로 path의 맨끝 파일명을 반환')
print(os.path.basename('/Users/Desktop/temp/test.txt'))

print('파일경로 path의 파일이름을 제외한 디렉토리 부분 반환')
print(os.path.dirname('/Users/Desktop/temp/test.txt'))

print('파일이 존재하는지 여부 -> True/False')
print(os.path.exists('/Users/Desktop/temp/test.txt'))

print('인수로 지정한 내용을 경로로 결합')
print(os.path.join("/Users/Desktop","Temp","test.txt"))

print('path에 대한 최근 변경시간을 반환한다. 파일이 없는 경우에는 error를 발생시킨다.')
print(time.gmtime(os.path.getatime(file_nm))) #최근접근시간
print(time.gmtime(os.path.getctime(file_nm))) #생성시간
print(time.gmtime(os.path.getmtime(file_nm))) #최근변경시간

print('파일의 크기리턴 -- 바이트단위')
print(os.path.getsize(file_nm))

print('디렉토리면 True')
print(os.path.isdir(file_nm), os.path.isdir(file_dir))

print('path에서 . / .. 과 같은 구분자를 제거해 path를 정규화시킨다. (=원래 path의 패턴으로 만들어 준다)')
print(os.path.normpath('/Users//Desktop/../temp/./test.txt'))

print('path를 디렉토리와 파일로 분리한다. tuple로 반환')
tpath = os.path.split(file_nm)
print(tpath, tpath[0], tpath[1])

# 이식성을 고려해서 'C:\\00.Dev\\Study\\Python\\00.LibExample\\00.String.py' 이렇게 하지말고
# join으로 연결해서 path만들어서 사용.....unix와 window고려
