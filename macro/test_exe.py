# 간단한 실행파일 테스트
# 인수로 base64인코딩된 json데이터를 받아서 디코딩한후 정보를 읽는다
# python 실행파일 만들기
# pip install pyinstaller
# 실행파일 만들기
# c:\Users\김태훈\AppData\Roaming\Python\Python311\Scripts\pyinstaller --onefile test_exe.py
# dist아래 실행파일 1개 생김

import sys
import json
import base64
import log
import psutil

logger = log.get_logger(name="EXEC_CALL", log_dir="c://upds_logs")

# 실제 실행되는 파일명
proc_name = 'test_exe.exe'


# 실행중인 프로세스 목록을 가져와 이미 실행중인지 체크한다.
# 이중실행 방지를 위해 만듬.
def proc_check():
    ps_cnt = 0
    for proc in psutil.process_iter():
        # 프로세스 이름을 ps_name에 할당
        ps_name = proc.name()
        logger.info("ps_name=%s pid=%d ppid=%d" % (ps_name, proc.pid, proc.ppid()))

        if ps_name == proc_name:
            logger.info("동일한 프로세스 명을 찾음!!!!!")
            ps_cnt += 1
    return ps_cnt


def main(run_info: str):
    # print('전달받은 인수값 = ')
    # print(run_info)

    param = json.loads(run_info)
    logger.info("VERSION=%s" % (param['VERSION']))
    logger.info("ACNT_NO=%s" % (param['ACNT_NO']))
    logger.info("CMD=%s" % (param['CMD']))
    logger.info("DATA1=%s" % (param['DATA1']))
    # time.sleep(600)
    return


# main 시작점을 시작하게 한다.
if __name__ == "__main__":
    logger.info('main_process')
    logger.info(sys.argv)

    # 프로그램 실행여부 체크
    # ps_cnt = proc_check()
    # logger.info("프로그램 실행 카운트 : %d" % ps_cnt)
    # 프로세스 카운트가 2개 나옴 추후 확인할 것
    # if ps_cnt >  1:
    #     logger.info('이미 프로그램이 실행중입니다.')
    #     sys.exit()


    if len(sys.argv) != 2:
        logger.info('전달받을 인수가 필수입니다.')
        sys.exit()
    else:
        # 받은 인수는 upds://[base64인코딩문자열]
        # upds://를 분리한다.
        run_info = sys.argv[1].split('//')[1]
        str_bytes = base64.b64decode(run_info)
        json_data = str_bytes.decode('ascii')
        logger.info(json_data)
        main(json_data)