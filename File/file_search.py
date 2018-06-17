
# 지정 디렉토리에서 특정 파일을 검색

import os

# def file_search(dir_name, file_name):
#     filenames = os.listdir(dir_name)
#
#     for filename in filenames:
#
#         full_filename = os.path.join(dir_name, filename)
#         # print(full_filename)
#         if os.path.isdir(full_filename):
#             f = file_search(full_filename, file_name)
#         else:
#             file_nm = os.path.split(os.path.splitext(full_filename)[0])[-1]
#             ext = os.path.splitext(full_filename)[-1]
#             if file_nm + ext == file_name:
#                 print(full_filename)
#                 return full_filename

# 특정 디렉토리 아래의 파일을 검색해서 full-path와 파일명을 리턴한다.
# 개발자 local의 파일의 위치를 찾는다.

def file_search(dir_name, file_name):
    """
    :param dir_name: 찾기 시작할 디렉토리 위치 / 개발자 작업 디렉토리
    :param file_name: 찾으려는 파일명
    :return:
    """
    for (path, dir, files) in os.walk(dir_name):
        for filename in files:

            if filename == file_name:
                return "%s/%s" % (path, filename)


if __name__ == '__main__':
    f = file_search('D:\STUDY\pythonProject', 'ch10-1.txt')
    print(f)


