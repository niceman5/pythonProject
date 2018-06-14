#
# # ch10-1파일을 읽어 단어수 count 첫라인이 #은 skip
# with open('ch10-1.txt', 'r') as f:
#     l = f.readlines()
#     line_cnt = 0
#     for line in l:
#         line_cnt += 1
#         if line.startswith('#'):
#             print(line_cnt, ': 0')
#             continue
#         else:
#             n = len(line.split())
#             print(line_cnt, ':', n)
#


# # file을 읽어서 sort
# 이건 \n처리가 안됨
# with open('ch10-2.txt', 'r') as f:
#     l = f.readlines()
# l.sort()
# for line in l:
#     print(line)
#
# with open('ch10-2.txt', 'r') as f:
#     l = f.read().splitlines()
#     l.sort()
#
# for line in l:
#     print(line)
#
# print('\n'.join(l))     #위의 반복과 동일한 효과

# # ch10-2.txt의 두번째 단어를 기준으로 정렬
# with open('ch10-2.txt', 'r') as f:
#     l = f.read().splitlines()
#     print(l)
# l.sort(key=lambda a:a.split()[1])
# print('\n'.join(l))

# # ch10-2.txt의 읽어서 3개씩 출력
# with open('ch10-2.txt', 'r') as f:
#     l = f.read().split()
#     print(l)
#     lc = 0
#     for s1 in l:
#         lc += 1
#         if lc % 3 == 0:
#             print(s1)
#         else:
#             print(s1, ' ', end='')
#     print()
#     for k in range(0, len(l), 3):
#         print(' '.join(l[k:k + 3]))
# 

# weblog에서 특정 ip로 접근한 정보를 구분한다.
group = {}
print(group, type(group))
with open('weblog.txt', 'r') as f:
    l = f.readlines()

    for line in l:
        ip, url, tm = line.split(':')
        # print(ip, url, tm)

        # group dict에 ip라는 key가 없으면 dict에 추가한다.
        if ip not in group:
            group[ip] = []
        # group dict에 ip의 key에 내용을 추가한다.
        group[ip].append(url)

print(group)
import collections
for ip in group:
    print('-' * 80, '\n', ip)
    print(collections.Counter(group[ip]))
    # for url, cnt in collections.Counter(group[ip]).items():
    #     print('{} {}'.format(url, cnt))









