import hashlib, os, sys

#
# Main Process 시작
#
if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('HASH검사할 파일명을 입력')
        sys.exit(1)

    file_name = sys.argv[1]

    hasher = hashlib.md5()
    with open(file_name, 'rb') as f:
        f_cont = f.read()
        hasher.update(f_cont)

    print(hasher.hexdigest())