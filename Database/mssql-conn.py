from openpyxl import Workbook
import pyodbc
import sys

#
# Main Process 처리
#
if __name__ == '__main__':
    wb = Workbook()

    # 현재 Active Sheet 얻기
    ws = wb.active

    # 엑셀의 제목을 기록한다.
    ws.append(['사용자번호', '이름', '회사명', '지점명', '핸드폰번호', '서비스상태','과금상태', '소식전하기-SMS', \
               '소식전하기-MMS', '소식전하기-메일', \
               '월간안부발송', '기념일발송', '감사안부발송', '테마발송', '로그인건수', '발송고객수', '미발송고객수',\
               '기념일갯수', '연속사용개월', '사용요금제', '가입일', '서비스개시일'])

    server = ''
    database = 'ubis'
    username = 'ubis'
    password = 'ubis'
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = conn.cursor()

    sql = """\
    DECLARE @RC int;
    EXEC @RC = ubis.dbo.upADMIN_USER_EXCEL_LIST @VIEW_TYPE=1, @VIEW_MONTH=NULL;
    SELECT @RC AS rc;
    """
    values = (3)
    cursor.execute(sql, (values))
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        print("Record not found.")
        sys.exit(1)
    
    # print(rows, type(rows))
    for row in rows:
        ws.append(list(row))
        # print(row)
        # print(type(rows))
    
    wb.save("sample.xlsx")
    conn.close();

