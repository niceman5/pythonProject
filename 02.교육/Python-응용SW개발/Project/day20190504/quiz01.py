# cnt = 1
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(cnt, end=' ')
#         cnt = cnt + 1
#     print()

cnt = 1
with open('D:\\PythonProject\\Project\\day20190504\\gugudan.txt', 'a') as f:
    # for i in range(1, 11):
    #     for j in range(1, 11):
    #         # print(cnt, end=' ')
    #         f.write(str(cnt) + ' ')
    #         cnt = cnt + 1
    #     # print()
    #     f.write('\n')
    for i in range(1, 101):
        f.write('{0:>4}'.format(i))
        if i % 10 == 0:
            f.write('\n')
