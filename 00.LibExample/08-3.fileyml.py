#-*-coding: utf-8

# pip install PyYAML
import yaml
import sys
from pathlib import Path
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



root_dir = Path('C:\\')
file_dir = root_dir / '00.Dev' / 'study' / 'Python' / '00.LibExample' / 'file'
yml_file = file_dir / 'sample.yml'

print(yml_file)

f_yml = open(yml_file, 'r')
conf = yaml.load(f_yml)
print(conf, type(conf))
f_yml.close()

print(conf['database']['port'], type(conf['database']['port']))

# ymal파일중 '---'로 구분된 파일을 읽을때는 load_all
yml_file2 = file_dir / 'sample2.yml'
with open(yml_file2, 'r') as f:
    for data in yaml.load_all(f):
        print(data, type(data))

hosts = {'web_server':['192.168.0.2','192.168.0.3'], 'db_server':['192.168.10.7'], 'link_server':['테스트']}
print(hosts, type(hosts))        

yml_file3 = file_dir / 'sample3.yml'


# 한글 부분은 차후 확인후 해결 할것

with open(yml_file3, 'w', encoding='utf-8') as f:
    # f.write(yaml.dump(hosts, default_flow_style=False))
    txt = yaml.dump(hosts, default_flow_style=False, stream=None)
    print(txt, type(txt))    
    f.write(txt)
    txt2 = txt.encode("utf-8")
    print(txt2)
    
    