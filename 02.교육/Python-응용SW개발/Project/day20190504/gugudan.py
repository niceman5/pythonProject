file = open('D:\\PythonProject\\Project\\day20190504\\gugudan.txt', 'w')

for i in range(2, 10):
    for j in range(1, 10):
        file.write('{} * {} = {}\n'.format(i, j , i*j))
        print('{} * {} = {}'.format(i, j , i*j))
    print()
    file.write('\n')
file.close()
