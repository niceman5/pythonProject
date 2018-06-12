import logging




# 1) logger 라는 인스턴스를 생성
# - logging.getLogger() 로 생성
# - getLogger() 와 같이 이름을 넣지 않으면 root logger 가 생성되며
# - getLogger('dev') 등의 이름을 넣으면 해당 이름의 logger 가 생성된다. root, dev 등은 모듈네임이 된다.
# 
# 2) setLevel()  을 이용하여 레벨을 설정한다
# - DEBUG, INFO, WARNING, ERROR, CRITICAL 중 선택이 가능하며, custom level 도 설정이 가능하다
# - 레벨을 설정하면 그 레벨을 포함함 상위레벨이 출력된다.
# - DEBUG 설정시 DEBUG, INFO, WARNING, ERROR, CRITICAL출력
# - INFO 설정시 INFO, WARNING, ERROR, CRITICAL 출력
# - ERROR 설정시 ERROR, CRITICAL 출력
# - handler 에서 설정한 level 은 logger 에서 설정한 level 아래로 적용되지 않는다
# - logger 에서 ERROR 로 설정하였다면 handler 에서 INFO 로 설정하여도 ERROR 이상만 출력됨
# * 아래에 좀더 살펴볼 예정

# main process시작
if __name__ == '__main__':
    logger = logging.getLogger()        # create logger instance
    logger.setLevel(logging.DEBUG)      # handler level 


    #  핸들러를 3개 만들어서 logger 에 추가
    test_formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')

    #create handler stdout
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)      # 가각 handler별로 레벨을 틀리게 줄수 있다.
    logger.addHandler(stream_handler)

    #file에 로그를 기록
    file_handler = logging.FileHandler('log.log')
    file_handler.setFormatter(test_formatter)
    file_handler.setLevel(logging.ERROR)
    logger.addHandler(file_handler)

    #file 로그에 기록2
    file_debug_handler = logging.FileHandler('log_debug.log')
    file_debug_handler.setFormatter(test_formatter)
    file_debug_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_debug_handler)

    # loging Test
    logger.debug("a debug")
    logger.info("a info")
    logger.warning("a warning")
    logger.error("a error")
    logger.critical("a critical")
    logger.info("-"* 80)


# logger를 다른 모듈에서 사용
# -> 방금 테스트한 것을 다른 모듈(=다른 파일)에서 바로 사용

# import logging
# logger = logging.getLogger(__name__)

