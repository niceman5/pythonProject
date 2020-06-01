import logging

if __name__=='__main__':
    logging.debug('debug message')      # 출력안됨
    logging.info('info message')        # 출력안됨
    logging.warning('warning message')
    f_thing = '에러 메시지.'
    logging.error('I love %s', f_thing)


    '''
    파이썬 로깅의 기본 설정은 WARNING 입니다. 따라서  DEBUG < INFO < WARNING < ERROR < CRITICAL  
    이 순서에서 더 높은 레벨인 ERROR 는 출력이 되지만, 하위레벨 (INFO,DEBUG) 은 출력이 안됩니다.
    즉 이 레벨을 DEBUG 나 INFO 로 낮추어 설정 한후에 사용해야 합니다. 설정하는 방법은 조금 있다가 살펴보죠.
    '''
    mylog = logging.getLogger('my')
    mylog.setLevel(logging.INFO)
    mylog.debug('debug message')      # 출력안됨
    mylog.info('info message')        # 출력됨

    file_handler = logging.FileHandler('my.log')
    mylog.addHandler(file_handler)
    mylog.info("server start!!!")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    mylog.info("server start222!!!")

    '''
    asctime 시간
    name 로거이름
    levelname 로깅레벨 
    message 메세지 
    funcName    로그호출을 포함한 함수 이름
    module      모듈 이름
    path        로그를 호출한 파일의 전체 경로
    process     프로세스id
    thread      스레드id

    '''

    '''
    로깅 모듈 생성에 관한 고찰 

    자 위에서 나만의 로깅 객체를 만들 때 logging.getLogger("my") 라고 만들었었는데요.  
    그냥 매개변수 없이 logging.getLogger() or logging.getLogger("") 이렇게 만들 수도 있습니다. 

    이렇게 하면 루트로거 를 리턴하게 되며, 루트로거는 로깅시스템의 기본로거이고 기본레벨은 warning 을 가지고 있습니다. 우리가 젤 처음에 로거를 만들지 않고 그냥 logging.error("...") 
    식으로 사용했었죠? 내부에서는 루트로거를 사용하고 있답니다.

    로깅 생성에 대한 특성을 정리 해 보면 아래와 같습니다. 

    * logging.getLogger() 를 통해 루트 로거 얻어서 사용 할수 있습니다.(기본레벨은 warning)
    * logging.error() 를 직접 호출하면 내부에서 루트로거를 이용합니다.
    * Logger 인스턴스는 이름으로 식별됩니다.
    * 동일 모듈 뿐만 아니라, 여러 모듈에서 동일한 인스턴스이름 logging.getLogger('someLogger')를 여러 번 호출해도 동일한 로거 객체에 대한 참조가 반환됩니다.
    * 빈 문자열인 "" 라는 이름의 루트 로거가 있으며, 다른 Logger 들은 모두 루트 Logger 의 자식들입니다. 따라서 루트 로거에 기본적인 설정을 해두고 사용하면 자식들은 모두 동일한 설정을 
      사용하게 됩니다.(핸들러,포매터등) 
    * 이름은 마침표(.) 로 구분되는 문자열이며 계층 구조를 형성한다. 즉 a 라는 로거를 만들고, a.b 라는 로거를 만들면 a.b는 a 로거의 자식입니다. 
    * 하나의 모듈에서 상위 로거를 정의 및 구성하고 별도의 모듈에서 하위 로거를 생성 할 수 있으며 하위에 대한 모든 로거 호출은 상위 노드로 전달됩니다.
    * 가능하면 루트 로거를 사용하기 보다는 각 클래스나 모듈마다 별도의 로거를 만드는 것을 추천합니다.
    * 로깅 메세지는 부가정보가 합쳐져서 LogRecords 로 생성되며, 이 객체를 가지고 각각의 handler 는 파일,콘솔,TCP 등으로 로 emit (출력) 합니다
    
    
    로깅 모듈 생성 실제 - 로거 범위 

    보통 main 에서 로깅 시스템 (대표설정) 을 만들어서 사용하게 됩니다. 이것을 디폴트로 자식 로거들에서 사용하게 되며, 자식별로 필요하면 특정 설정을 하게 됩니다. 
    또한 핸들러는 버퍼링을 하고 있기 때문에 어플리케이션이 갑자기 중지되기 전에 logging.shutdown() 을 호출해서 모두 출력해 주면 좋습니다. (fianllly 절에서 수행) 

    https://hamait.tistory.com/880 참조
    '''

    '''
    저런 관계에 따른 이상 행동을 예측 하기 위해서는 부모/자식간의 행동을 파악할 필요가 있는데요.
    다음 코드를 보시죠. 
    # 루트 로거 생성 
    rootlogger = logging.getLogger()
    rootlogger.setLevel(logging.INFO)
    stream_hander = logging.StreamHandler()
    rootlogger.addHandler(stream_hander)

    # "my" 로거 생성 
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)
    stream_hander2 = logging.StreamHandler()
    mylogger.addHandler(stream_hander2)

    # "my" 로거 생성 
    mylogger.info("message from mylogger")

    루트로거를 a 모듈에서 만들고, "my" 로거를 다른 곳에서 만들었다고 칩시다.( 위에 소스에서는 보기 쉽게 같은 곳에 두었음)  "my" 로거에서 "message from mylogger" 를 출력 했는데, 
    결과는 어떻게 될까요? 

    message from mylogger
    message from mylogger

    이렇게 2개의 메세지가 출력되는데 상위로 전파되었기 때문입니다.
    이것을 막으려면, 간단하게는 루트로거에서 핸들러를 추가해 주지 않아도 되며, 혹은
    
    mylogger.propagate = 0
    propagate 를 0 으로 세팅하면 상위로 전파하지 않습니다.
    '''




    # logfmt = '%(asctime)s %(levelname)s %(message)s'
    # logging.basicConfig(
    #     # filename = 'C:\\DATA\Study\\pythonProject\\00.LibExample\\test.log',
    #     filename = '\\test.log',
    #     level=logging.DEBUG
    # ) 
    # logging.debug('debug message')
    # logging.info('info message')
    # logging.warning('warning message')

    # FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    # logging.basicConfig(format=FORMAT)    
    # d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    # logger = logging.getLogger('tcpserver')
    # logger.warning('Protocol problem: %s', 'connection reset', extra=d)


