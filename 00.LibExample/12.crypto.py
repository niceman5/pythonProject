# pip install pycryptodedome
# python 버젼 3이상은 pycryptodedome 설치
# https://pycryptodome.readthedocs.io/en/latest/ 참조할것

import hashlib
from crypto.Hash import SHA512

if __name__ == '__main__':
    # 해시값 생성
    hash_md5 = hashlib.md5(b'hamegg')
    aa = hash_md5.hexdigest()
    print(aa, type(aa))

