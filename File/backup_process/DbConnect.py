'''
Program id  :   dbconnect.py
Description :   python mssql connect모듈               

    1)관리자에게 sms/mms발송하는 기능
    2)db용 로그에 기록남기는 기능


    사전작업 
    * pyodbc 설치 ->  pip install pyodbc
    
    https://learn.microsoft.com/ko-kr/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16

    여기서 odbc 17버전 다운받아 설치. 18버전은 인증서 관련 문제가 있음. 17버젼으로 확인
    설치된 프로그램에 odbc설치되었는지 확인


Author		: 김태훈
Create Date : 2023-05-17

History
'''

import pyodbc

class DbConnect():

    # 생성자, db연결
    def __init__(self,IP, DB, UID, PW ):
        con_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+IP+';DATABASE='+DB+';UID='+UID+';PWD='+PW
        print(con_str) 
        self.conn = pyodbc.connect(con_str)            
        self.cursor = self.conn.cursor()
        print('db - connect')    
    # 소멸자 : 리소스 해제 
    def __del__(self) :        
        self.conn.close()
        print('db - close')

    def setLogger(self, log):
        self.logger = log

    # 관리자에게 sms/mms문자로 각종 알림 발송
    def AdminUmsAlert(self, log_text='', send_type = 0, send_number = None, media_type='SMS'):
        # EXEC dbo.upBatchLogMessageInsert
		#	@LogText		= @LogText
		#,   @SendType		= 0			--0:개발팀 1:개발팀+임원 2:운영팀 3:개발팀장+본부장님
		#,   @SendNumber     = NULL
		#,	@MEDIA_TYPE		= 'MMS'
        sql = """
        EXEC UBIS.dbo.upBatchLogMessageInsert
			@LogText		= ?
		,   @SendType		= ?			--0:개발팀 1:개발팀+임원 2:운영팀 3:개발팀장+본부장님
		,   @SendNumber     = ?
		,	@MEDIA_TYPE		= ?
        """
        values = (log_text, send_type, send_number, media_type)
        self.cursor.execute(sql, (values) )
        
        if self.cursor.rowcount > 0:                
            self.conn.commit()        
            self.logger.info('AdminUmsAlert : Mesg[{0}] send_type={1}'.format(log_text, send_type) )
        else:
            self.conn.rollback()        
            self.logger.info('AdminUmsAlert - Rollback : Mesg[{0}] send_type={1}'.format(log_text, send_type) )

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
        self.cursor.execute(sql, [proc_name, error_line, error_mesg ]  )
        # self.logger.info(self.cursor.rowcount)
        
        if self.cursor.rowcount > 0:            
            self.conn.commit()                
            self.logger.info('BatchError : proc_name[{0}] error_mesg=[{1}]'.format(proc_name, error_mesg) )
        else:
            self.conn.rollback()                
            self.logger.info('BatchError - Rollback: proc_name[{0}] error_mesg=[{1}]'.format(proc_name, error_mesg) )
        

    # BatchLog를 남긴다.
    # BatchLog를 남겨 배치실행 체크하는 배치에서 실행여부를 관리자에게 통보한다.
    def BatchLog(self, ProcessNo, LogText):
        # UBIS.dbo.upBatchLogMessageInsert 
        #   @ProcessNo		INT
        #,	@LogText		VARCHAR(MAX)
        #,	@Result			INT OUTPUT
        sql = """
        DECLARE @RESULT INT;

        EXEC UBIS.dbo.upBatchLogInsert
			@ProcessNo		= ?
		,   @LogText		= ?					
		,	@Result		    = @RESULT   OUTPUT
        SELECT @RESULT  AS RESULT
        """        
        self.cursor.execute(sql, [ProcessNo, LogText] )        
        row = self.cursor.fetchone()      
        # self.logger.info( row[0] )
                
        if row[0] > 0:
            self.conn.commit()                  
            self.logger.info('BatchLog : ProcessNo[{0}] LogText=[{1}]'.format(ProcessNo, LogText) )
        else:
            self.conn.rollback()
            self.logger.info('BatchLog - Rollback : ProcessNo[{0}] LogText=[{1}]'.format(ProcessNo, LogText) )
            
        return row[0] 