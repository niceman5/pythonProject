file = open('D:\\PythonProject\\Project\\day20190504\\gugudan.txt', 'r')

# for line in file.readlines():
#     print(line, end='')

# while True:
#     text = file.readline()
#     if not text:        # 파일이 끝이면 종료
#         break
#     print(text, end='')


# 한번에 읽는다.
text = file.read()
print(text)

file.close()
print('success!!!!')
