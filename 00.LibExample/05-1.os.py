import os

print('os.environ=', os.environ['HOME'])    # home디렉토리
print('os.getcwd()=',os.getcwd())       # 현재 작업중인 디렉토리
print(os.listdir())
os.chdir('..')
print(os.listdir())
os.chdir('c:\\')
print(os.listdir())
print(os.cpu_count())