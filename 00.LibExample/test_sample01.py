import pytest

# test 실행
# py.test test_sample01.py
# 파일명이 test_*또는 *_test로 되어 있어야 실행됨
# py.test [테스트가 저장된 디렉토리]
# def test_upper():
#     assert 'foo'.upper() == 'FOO'

@pytest.mark.parametrize('obj',['1','2','Foo'])
def test_isdigit(obj):
    assert obj.isdigit()
    