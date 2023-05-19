'''
Program id  :   dbconnect.py
Description :   python mssql connect 및 db를 통한 SMS/MMS알림 로그 기록용 모듈

    MSSQL 사용을 위한 사전작업 
    * pyodbc 설치 ->  pip install pyodbc
    * DDBC드라이버 설치       
    .. 
        https://learn.microsoft.com/ko-kr/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16        
        여기서 odbc 17버전 다운받아 해당 python모듈이 실행될 서버에 설치. 
        mssql-18버전은 인증서 관련 문제가 있어서 17버젼으로 설치해야 함
        설치된 프로그램에 odbc드라이버가 설치되었는지 확인

    * pyodbc설명은 https://github.com/mkleehammer/pyodbc 참조
Author		: 김태훈
Create Date : 2023-05-17

History
'''

import pyodbc
import sys

class DbConnect():

    # 생성자, db연결
    def __init__(self,IP, DB, UID, PW ):
        con_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+IP+';DATABASE='+DB+';UID='+UID+';PWD='+PW
        # print(con_str) 
        try :            
            self.conn = pyodbc.connect(con_str)            
            self.cursor = self.conn.cursor()
            print('DbConnect - connect!')    
        except Exception as e:
            print(e)
            sys.exit('db connection Error!!')

    # 소멸자 : 리소스 해제 
    def __del__(self) :  
        try :                  
            self.conn.close()            
            print('DbConnect - connection close!')
        except Exception as e:
            print(e)
            sys.exit('db connection close Error!!')            

    def setLogger(self, log):
        self.logger = log

    def AdminUmsAlert(self, log_text='', send_type = 0, send_number = None, media_type='SMS'):
        """관리자에게 sms/mms문자로 각종 알림 및 경고내용을 발송한다.
        
        Args: 
            log_text  : 발송할 로그 메시지
            media_type  : SMS/MMS 발송 매체를 구분한다.
            send_number : None이면 회사번호로 발송
            send_type : 0:개발팀 1:개발팀+임원 2:운영팀 3:개발팀장+본부장님
        
        Returns:
            없음:        
        
        참고:
            주석은 이런식으로
        """        
        
        sql = """
        EXEC UBIS.dbo.upBatchLogMessageInsert
			@LogText		= ?
		,   @SendType		= ?			--0:개발팀 1:개발팀+임원 2:운영팀 3:개발팀장+본부장님
		,   @SendNumber     = ?
		,	@MEDIA_TYPE		= ?
        """
        values = (log_text, send_type, send_number, media_type)
        
        # 정상실행되면 commit찍고 아니면 rollback        
        # count에는 영향받은 row건수 
        try:            
            count = self.cursor.execute(sql, (values) ).rowcount
        except pyodbc.DatabaseError as err:
            self.conn.rollback()        
            self.logger.debug(err)
            self.logger.info('AdminUmsAlert - Rollback : Mesg[{0}] send_type={1}'.format(log_text, send_type) )
        else:
            self.conn.commit()        
            self.logger.info('AdminUmsAlert : Mesg[{0}] send_type={1} rowcount={2}'.format(log_text, send_type, count) )
        finally:
            pass

    # BatchError를 남긴다.
    # 실행하는 작업이 배치작업인데 오류가 발생했을 경우 배치오류기록을 남겨 관리자가 확인할수 있게 한다.
    def BatchError(self, proc_name='DbConnect.py', error_line=0, error_mesg=''):
        sql = """
        INSERT INTO dbo.BatchError
        (
            ErrorDate
        ,   ErrorProcedure
        ,   ErrorNumber
        ,   ErrorSeverity
        ,   ErrorState
        ,   ErrorLine
        ,   ErrorMessage        
        )
        VALUES
        (   
            GETDATE()
        ,   ?
        ,   0
        ,   0
        ,   1
        ,   ?
        ,   ?
        )
        """        
        try :
            count = self.cursor.execute(sql, [proc_name, error_line, error_mesg ]).rowcount
        except pyodbc.DatabaseError as err:
            self.conn.rollback()       
            self.logger.debug(err)         
            self.logger.info('BatchError - Rollback: proc_name[{0}] error_mesg=[{1}]'.format(proc_name, error_mesg) )            
        else:
            self.conn.commit()                
            self.logger.info('BatchError : proc_name[{0}] error_mesg=[{1}] rowcount={2}'.format(proc_name, error_mesg, count) )
        finally:
            pass
        
    # BatchLog를 남긴다.
    # BatchLog를 남겨 배치실행 체크하는 배치에서 실행여부를 관리자에게 통보한다.
    # RETURN Type : {'RESULT' : 1} dict로 리턴한다.
    def BatchLog(self, ProcessNo, LogText):
        sql = """
        DECLARE @RESULT INT;

        EXEC UBIS.dbo.upBatchLogInsert
			@ProcessNo		= ?
		,   @LogText		= ?					
		,	@Result		    = @RESULT   OUTPUT
        SELECT @RESULT  AS RESULT
        """  
        
        try :      
            self.cursor.execute(sql, [ProcessNo, LogText] )        
            row = self.cursor.fetchone()      
            # self.logger.info( row[0] )
        except pyodbc.DatabaseError as err:                    
            self.conn.rollback()
            self.logger.debug(err)
            self.logger.info('BatchLog - Rollback : ProcessNo[{0}] LogText=[{1}]'.format(ProcessNo, LogText))
            return {'RESULT' : 0}
        else:
            self.conn.commit()                  
            self.logger.info('BatchLog : ProcessNo[{0}] LogText=[{1}] rowcount={2}'.format(ProcessNo, LogText, row[0]) )
            return {'RESULT' : row[0]}
        finally:
            pass