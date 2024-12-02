import configparser as parser


#
# Main Process 처리
#
if __name__ == '__main__':

    # config 파일 읽기
    config = parser.ConfigParser()
    config.read('./config.ini')

    path_config = config['PATH']

    root_path = path_config['root_path']
    work_path = path_config['work_path']

    print(root_path)
    print(work_path)


