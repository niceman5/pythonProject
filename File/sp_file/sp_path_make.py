import os
import sys
import configparser as parser

"""
SP파일명을 가지고 SP적용처리할 파일 목록을 만든다.
입력파일에는 sp명에 "aaaa"이렇게 들어가 있고 이걸 가지고 기준 디렉토리를

sys.argv[2] : input file name (소스를 찾을 파일명) 이름이 없으면 input.txt가 된다.
sys.argv[3] : output file name 이름이 없으면 output.txt가 된다.

ex)
py file_path_make.py [input.txt] [output.txt]
"""
# 특정 디렉토리 아래의 파일을 검색해서 full-path와 파일명을 리턴한다.
# 개발자 local의 파일의 위치를 찾는다.

def file_search(root_path, sp_lists):
    """
    :param dir_name: 찾기 시작할 디렉토리 위치 개발자 작업 디렉토리
    :param file_name: 찾으려는 파일명
    :return:
    """
    out_files = []
    find_val = -1

    # sp파일별로 디렉토리에서 파일을 찾는다.
    for sp_filename in sp_lists:
        find_val = -1

        for (path, dir, files) in os.walk(root_path):
            for filename in files:
                # directory에서 찾은 파일명을 소문자로 변경한다.
                org_file_nm = filename.lower()

                # sp파일명과 물리 파일명 비교해서 포함되는지 확인
                # 포함되면 flag값 설정하도 out-list에 추가한다.
                if org_file_nm.find(sp_filename) >= 0:
                    find_val = 1
                    out_files.append(path + org_file_nm)
                    print(f"{sp_filename} = {path + org_file_nm}")

        #  out-list에 추가된게 없으면 파일 못 찾았다고 기록한다.
        if find_val == -1 :
            out_files.append(sp_filename + ": NOT FOUND!!!!! ")
            print(f"{sp_filename} : NOT FOUND!!!!!")
    
    return out_files

#
# Main Process 처리
#
if __name__ == '__main__':

    # config 파일 읽기
    config = parser.ConfigParser()
    config.read('./config.ini', encoding='utf-8')

    path_config = config['PATH']

    # sp검색을 시작하는 root디렉토리
    root_path = path_config['root_path']
    # input-file, output-file의 위치
    work_path = path_config['work_path']

    in_file = ''
    out_file = ''
    if len(sys.argv) == 1:
        in_file = 'Input.txt'
        out_file = 'output.txt'
    elif len(sys.argv) == 2:
        in_file = sys.argv[1]
        out_file = 'output.txt'
    elif len(sys.argv) == 3:
        in_file = sys.argv[1]
        out_file =  sys.argv[2]
    else:
        print('사용예 > py file_path_make.py [input.txt] [output.txt]')
        sys.exit(1)

    in_file = work_path + '\\'+ in_file;
    out_file = work_path + '\\'+ out_file;
    print("sp파일 목록 생성-----------")
    print(f"root_path : {root_path}")
    print(f"work_path : {work_path}")
    print()
    print(f"in_file : {in_file}")
    print(f"out_file : {out_file}")

    sp_lists = []
    with open(in_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()     #공백을 제거한다.

            # 주석이나 공백라인은 sklip한다.
            if line.startswith('#') or len(line) == 0:
                continue

            # 파일에서 읽은 sp파일명을 list에 넣는다.
            sp_lists.append(line.lower())

    # file내용을 중복처리한다.
    sp_lists = list(set(sp_lists))

    # sp_file이 있는지 체크한다. 없으면 종료
    if len(sp_lists) == 0:
        print('찾으려는 sp파일이 없습니다.')
        sys.exit(1)

    # print(sp_lists)

    # sp 파일목록의 실제 파일을 찾는다....
    out_files = file_search(root_path, sp_lists)

    if len(out_files) == 0:
        print('생성한 sp파일목록이 없습니다.')
        sys.exit(1)
    else:
        # output파일에 기록한다.
        with open(out_file, 'w', encoding='utf-8') as out:
            for line in out_files:
                out.write(line + '\n')

