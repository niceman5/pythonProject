data = '''
park 010-1111-1111
kim 010-2222-2222
kim 010-222-2222
'''

# 전화번호만 추출
import re
# p = re.compile('[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
p = re.compile('\d{3}-\d{3,4}-\d{4}')

print('findall :', p.findall(data))
