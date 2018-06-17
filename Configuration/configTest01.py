import os
import sys
import configparser
import json


# Main 프로세스

if __name__ == '__main__':
    config = configparser.ConfigParser()

    # ini파일이 없을때 처리
    # config.read('config02.ini', encoding='UTF8')
    # print(config.sections())
    # if len(config.sections()) == 0:
    #     print("config02.ini 설정파일이 실행폴더에 없습니다.")
    #     sys.exit(1)

    # config.read('config01.ini', encoding='UTF8')
    # TEST = config['TEST']
    # print(TEST.get('ID'))
    # print(TEST.get('EMAIL'))

    # default는 안나옴
    # id = config['DEFAULT']['ID']        # 'ID'
    # EMAIL = config['DEFAULT']['EMAIL']  # 'EMAIL'
    #
    # print(id, type(id))
    # print(EMAIL, type(EMAIL))
    #
    # id = config['TEST']['ID']        # 'ID'
    # EMAIL = config['TEST']['EMAIL']  # 'EMAIL'
    #
    # print(id, type(id))
    # print(EMAIL, type(EMAIL))
    #
    # print(config['DEFAULT'])

    # json 설정파일 이용
    with open('config01.json', 'r', encoding='UTF8') as f:
        config = json.load(f)
        print(config)

        id = config['TEST']['ID']        # 'ID'
        EMAIL = config['TEST']['EMAIL']  # 'EMAIL'

        print(id, type(id))
        print(EMAIL, type(EMAIL))

        USERS = config['TEST']['USERS']
        print(USERS, type(USERS))

        for user in USERS:
            print(user['NAME'])
            print(user['AGE'])
