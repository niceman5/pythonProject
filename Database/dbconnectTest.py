# python에서 MSSQL연결
# 1. odbc드라이버를 설치한다.  https://www.microsoft.com/ko-kr/download/confirmation.aspx?id=56567
# 관리자 권한으로 cmd.exe를 엽니다.
# Pip-를 사용 하 여 pyodbc Python 패키지 관리자 설치
# pip install pyodbc

import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=TEST;UID=niceman5;PWD=gustnr35!')
cursor = conn.cursor()

# Sample select query
# 모든 data를 한번에 읽어서 처리
cursor.execute("SELECT [Std_No], [Name], [Age], [Sex], [LastChngDt] from test.dbo.Student;")
rows = cursor.fetchall()
for row in rows:
    print(row.Std_No, row.Name, row.Age, row.Sex, row.LastChngDt )
print('-' * 80)

# 파라메터를 전달해서 sql실행, list방식으로 전달한다.
cursor.execute(
    """
    SELECT [Std_No], [Name], [Age], [Sex], [LastChngDt] from test.dbo.Student WHERE Std_No=? AND name like ?;
    """, [3, '강%'] )
rows = cursor.fetchall()
for row in rows:
    print(row.Std_No, row.Name, row.Age, row.Sex, row.LastChngDt )



# 신규데이터 등록 commit이 안되면 반영안됨.
cursor.execute(
    """
    INSERT INTO Student ([Name], [Age], [Sex], [LastChngDt])
    VALUES ( ?, ?, ?, GETDATE())
    """, ['강강강', 50, True ] )
conn.commit()

# cursor.execute("delete from products where id <> ?", 'pyodbc')
# print('Deleted {} inferior products'.format(cursor.rowcount))
# cnxn.commit()
# deleted = cursor.execute("delete from products where id <> 'pyodbc'").rowcount
# cnxn.commit()

# connection을 종료한다.
conn.close();
