import os
import sys

# sys.argv[1] : 시작할 디렉토리 ex) d:\study
# sys.argv[2] : input file name (소스를 찾을 파일명) 이름이 없으면 input.txt가 된다.
# sys.argv[3] : output file name 이름이 없으면 output.txt가 된다.


# 특정 디렉토리 아래의 파일을 검색해서 full-path와 파일명을 리턴한다.
# 개발자 local의 파일의 위치를 찾는다.

def file_search(dir_name, file_name):
    """
    :param dir_name: 찾기 시작할 디렉토리 위치 / 개발자 작업 디렉토리
    :param file_name: 찾으려는 파일명
    :return:
    """
    # print(dir_name)
    # print(file_name)
    for (path, dir, files) in os.walk(dir_name):
        # print(path)
        # print(dir)
        # print(files)
        for filename in files:
            # comp_filename = filename[0,len(file_name)]
            if filename.lower()[0:len(file_name)] == file_name.lower():
                return "%s/%s" % (path, filename)

##
# Main Process 처리
#
if __name__ == '__main__':

    if len(sys.argv) < 4:
        print('1)시작할 디렉토리  2)input-file-name  3)output-file-name 을 입력되야 합니다.')
        sys.exit(1)

    start_dir = sys.argv[1]
    in_file = sys.argv[2]
    out_file = sys.argv[3]
    
    # print(start_dir, in_file, out_file)

    with open(out_file, 'w', encoding='utf-8') as out:
        with open(in_file, 'r', encoding='utf-8') as f:

            # 파일을 한줄씩 처리한다.
            for line in f.readlines():               

                line = line.strip()     # 공백을 제거한다.
                # 주석이나 공백라인은 sklip한다.
                if line.startswith('#') or len(line) == 0:
                    continue
                # print('line=%s' % line )

                file_name = file_search(start_dir, line)
                if file_name:
                    out.write(file_name + '\n')
                else:
                    out.write('###' + line + ' ---> NOT FOUND\n')
