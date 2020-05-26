import shutil

# 파일을 복사하고 복사한 파일명 리턴
a = shutil.copy('c:\\00.dev\\Study\\Python\\00.LibExample\\00.String.py', 'c:\\00.dev\\Study\\Python\\00.LibExample\\00.String.py1')
print(a)

# copytree 디렉토리 내용 복사하기...
# https://docs.python.org/ko/3/library/shutil.html?highlight=shutil#module-shutil

'''
shutil.rmtree(path , ignore_errors = False , onerror = None) 
    -> 디렉토리 삭제
shutil.move(src , dst , copy_function = copy2)
    -> 이동
shutil.disk_usage( 경로 ) 
    -> 지정된 경로에 대한 디스크 사용량 통계
shutil.chown( path , user = None , group = None ) 
    -> 소유자 변경, 그룹변경등
    

'''


