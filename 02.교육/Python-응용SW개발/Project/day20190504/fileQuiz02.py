
with open('D:\\PythonProject\\Project\\day20190504\\userInputData.txt', 'a') as f:
    while True:
        s1 = input('기록할 데이터 입력:')
        if s1 == '':
            print("종료")
            break
        else:
            f.write(s1+'\n')
