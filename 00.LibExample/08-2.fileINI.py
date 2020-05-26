from configparser import ConfigParser
from pathlib import Path


root_dir = Path('C:\\')
file_dir = root_dir / '00.Dev' / 'study' / 'Python' / '00.LibExample' / 'file'
ini_file = file_dir / 'config.ini'
config = ConfigParser()

a = config.read(ini_file)
print(a, type(a), len(a))

if len(a) > 0  :
    print('ini 파일 open')

sec = config.sections()
print(sec, type(sec), len(sec))

print(config.options('USER_A'))
# print(config.options('USER_B'))
# print('USER_B' in config)
if ('USER_B' in config) == False:
    print('해당 섹션이 없음')

print(config.get('USER_A', 'limit'))
# mail_dir = %(home_dir)s\mail 를 처리 $()s
print(config.get('USER_A', 'mail_dir'))
#user-section에 값이 없어서 default의 값을 사용한다.
print(config.get('USER_A', 'user_dir'))