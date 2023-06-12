"""pyodbc를 이용한 mssql class module

MSSQL 사용을 위한 사전작업
* pyodbc 설치 ->  pip install pyodbc
* DDBC드라이버 설치
..
    https://learn.microsoft.com/ko-kr/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16
    여기서 odbc 17버전 다운받아 해당 python모듈이 실행될 서버에 설치.
    mssql-18버전은 인증서 관련 문제가 있어서 17버젼으로 설치해야 함
    설치된 프로그램에 odbc드라이버가 설치되었는지 확인

* pyodbc설명은 https://github.com/mkleehammer/pyodbc 참조

개발자  : 김태훈
작성일  : 2023-05-17
수정이력
"""
import pyodbc
import sys


class db:
    """ mssql 작업용 클래스
    Stored Procedure호츨과 SQL직접 호출관련 인터페이스를 제공하고 결과를 list형태로 반환한다.
    """
    def __init__(self):
        pass

    def __del__(self):
        try:
            self.conn.close()
            print('DbConnect - connection close!')
        except Exception as e:
            print(e)
            sys.exit('db connection close Error!!')

    def connect(self, IP: str, DB: str, UID: str, PW: str):
        """ Database에 연결한다.
        """
        str_set = ['DRIVER={ODBC Driver 17 for SQL Server};SERVER=', IP,
                   ';DATABASE=', DB,
                   ';UID=', UID,
                   ';PWD=', PW]
        con_str = "".join(str_set)
        # print(con_str)
        try:
            self.conn = pyodbc.connect(con_str)
            self.cursor = self.conn.cursor()
            print('DbConnect - connect!')
        except Exception as e:
            print(e)
            sys.exit('db connection Error!!')

    def setLogger(self, log):
        """
        db처리관련 log를 남기기 위한 log인스터스 지정한다.
        """
        self.logger = log

    def exec_sp(self, sp_name: str, params: dict) -> list:
        """Stored Procedure 호출용 함수

        Args:
            sp_name (string) : 프로시져 명. 'UBIS.DBO.SP_NAME' 식으로 써야 함
            params (dict) : 넘겨질 파라메터 dict형태로 받는다. {"Name":"가나다"}
                null값을 사용할때는 {"Age":None} 으로 사용한다.

        Returns :
            결과 rowset을 모두 list에 담아 return한다.
        """
        pass
