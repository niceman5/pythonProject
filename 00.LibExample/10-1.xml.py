import xml.etree.ElementTree as et
from pathlib import Path

#  pip install lxml
# xml에 손상이 가도 읽음.....parse를 지정할수 있음
from lxml import etree


root_dir = Path('C:\\')
file_dir = root_dir / '00.Dev' / 'study' / 'Python' / '00.LibExample' / 'file'
xml_file  = file_dir / 'sample.xml'

tree = et.parse(xml_file)
print(1, tree, type(tree))
country = tree.find('./country')
print(2, country.tag)    #요소이름 얻기
print(3, country.attrib) #속성리스트 얻기
print(4, country.get('name'))

country_rank = country.find('./rank')
print(5, country_rank.tag)    #요소이름 얻기
print(6, country_rank.text)     #값읽기

el = tree.findall('./country')
for e in el:
    print(e.attrib, type(e))


xml_file  = file_dir / 'errxml.xml'
print(Path.exists(xml_file))
# xml 파싱중 에러남
# tree = etree.parse(xml_file)
# # Traceback (most recent call last):
# #   File "10-1.xml.py", line 29, in <module>
# #     tree = etree.parse(xml_file)
# #   File "src\lxml\etree.pyx", line 3519, in lxml.etree.parse
# #   File "src\lxml\parser.pxi", line 1862, in lxml.etree._parseDocument
# # TypeError: cannot parse from 'WindowsPath'

parser = etree.XMLParser(recover=True)
tree = etree.parse(xml_file, parser=parser)
# print(tree.find('./country'))