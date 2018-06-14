
# # 파일을 열고 내용을 기록하고 자동으로 닫는다.
# # try, finally보다 with를 사용하는게 낫다.
# with open('t1.txt', 'w', encoding='utf-8') as f:
# 	f.write('test')
#
# f1 = open('t1.txt')
# print(f1, type(f1))
# s = f1.read()
# print(s)
# f1.close()
#
# # 위의 코딩보다 간단하게 구현 가능하다.
# with open('t1.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
#
# lines = ['첫번째 라인\n', '두번째 라인\n', '세번째 라인\n']
# with open('t2.txt', 'w', encoding='utf-8') as f:
#     f.writelines(lines)         # list에 있는걸 한번에 wirte
#     f.write(''.join(lines))     # 위와 같은 코드임
#

# # 파일을 한줄씩 읽는다.
# with open('t2.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')

# # 파일을 한줄씩 읽는다.
# with open('t2.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()
#     while line:         # line이 없을때까지 읽는다.
#         print(line, end='')
#         line = f.readline()

# # 파일을 한번에 줄단위로 읽어서(list) 한줄씩 처리
# with open('t2.txt', 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line, end='')

# # 파일을 읽어서 단어수를 count
# import os
# with open('t2.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#     print(s)
#     print('파일의 문자수 =', len(s))       # 파일의 문자수
#     print('파일의 크기 =', os.path.getsize('t2.txt'))  # 파일의 크기
#
#     n = len(s.split())
#     print('파일의 단어수 =', n)
#
#     print('파일의 라인수 =', s.count('\n'))    # 파일의 줄수를 count 라인 맨뒤의 \n을 count한다.
#     # print(len(f.readlines()))    # 파일을 list로 받아서 list의 줄수를 count한다.
#

# 윈도/도스에서 라인 구분자....
# import os
# os.linesep
# '\r\n'
# 리눅스에서 구분자
# '\n'
#
# # 파일에서 특정 바이트만 읽기
# with open('t2.txt', 'r', encoding='utf-8') as f:
#     s = f.read(5)   # 바이트가 아니라 5글자임.
#     print(s)
#
# import sys
# print(sys.stdout.encoding)
# print(sys.stderr.encoding)
#
# with open('t2.txt', 'rb') as f:
#     s = f.read()
#     b = bytes(s)
#     print(b, type(b))
#     # a = b.decode('euc-kr')
#
#

# file.close()        # 파일 close
# file.read([size])   # 원하는 바이트수 만큼 read,없으면 전체를 read, 파일 전체 read시 큰 파일의 경우 메모리 오버문제 있으니 끊어서 읽어야 함
# file.readline()     # 줄 하나 read, 바이트 지정하면 읽을수 있는 최대 바이트수가 된다.
# file.readlines()    # 전체줄을 readline을 통해 읽은 데이터를 list에 넣는다.
# file.write(str)     # 문자열 str을 파일에 쓴다.
# file.writelines(list)   # 문자열 리스트를 파일에 쓴다. 줄 바꾸기는 자동으로 들어가지 않는다.
#
# file.flish()        # 버퍼가 다 차지 않아도 내용을 파일에 쓴다.
# file.fileno()       # 파일 핸들 번호 리턴
# file.truncate([size])   # 파일크기를 지정한 크기로 잘라 버린다. 인수미지정시 현재 위치에서 자른다.
#
# file.closed         # 파일 닫혀있으면 1 아니면 0



