
#
# Stored procedure 사용
#

# id_ = 'test'
# pw = '12345'
# depart = 'none'
# class_ = 'GM'
# name = 'name'
# birthday = 'None'
# grade = 3
# subgrade = 2
#
# sql = 'exec [my_database].[dbo].[my_table](?, ?, ?, ?, ?, ?, ?, ?)'
# values = (id_, pw, depart, class_, name, birthday, grade, subgrade)
# cursor.execute(sql, (values))


# id_ = 'test'
# pw = '12345'
# depart = 'none'
# class_ = 'GM'
# name = 'name'
# birthday = 'None'
# grade = 3
# subgrade = 2
#
# sql = """\
# DECLARE @RC int;
# EXEC @RC = [my_database].[dbo].[my_sp] ?, ?, ?, ?, ?, ?, ?, ?;
# SELECT @RC AS rc;
# """
# values = (id_, pw, depart, class_, name, birthday, grade, subgrade)
# cursor.execute(sql, values)
# rc = cursor.fetchval()  # pyodbc convenience method similar to cursor.fetchone()[0]

# Don't forget SET NOCOUNT ON in your stored procedure.
#
# id_ = 'test'
# pw = '12345'
# depart = 'none'
# class_ = 'GM'
# name = 'name'
# birthday = 'None'
# grade = 3
# subgrade = 2
#
# sql = """\
# DECLARE @RC int;
# EXEC [my_database].[dbo].[my_sp] @RC OUTPUT, @id_=?, @pw=?, @depart=?, @class_=?, @name=?, @birthday=?, @grade=?, @subgrade=?;
# SELECT @RC AS rc;
# """
# values = (id_, pw, depart, class_, name, birthday, grade, subgrade)
# cursor.execute(sql, values)
# rc = cursor.fetchval()




import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=TEST;UID=niceman5;PWD=gustnr35!')
cursor = conn.cursor()

std_no = 3
cnt = 0
sql = 'exec dbo.sp_call_test02 ?, ?'
values = (std_no, cnt)
cursor.execute(sql, (values))
print(cursor, type(cursor))

rows = cursor.fetchall()
if len(rows) == 0:
        print("Record not found.")

print(rows, type(rows))
for row in rows:
    print(row.Std_No, row.Name, row.Age, row.Sex, row.LastChngDt )

print('-' *80)
# multi result set처리...
if cursor.nextset() == True:
    rows = cursor.fetchall()
    for row in rows:
        print(row.Std_No, row.Name, row.Age, row.Sex, row.LastChngDt)
#
# sql = """
# DECLARE @RC int;
# EXEC @RC = dbo.sp_call_test02 ?, ?;
# SELECT @RC AS rc;
# """
# std_no = 3
# cnt = 0
# values = (std_no, cnt)
# cursor.execute(sql, values)
# rc = cursor.fetchval()  # pyodbc convenience method similar to cursor.fetchone()[0]
# # 이건 문제 있음 실제 리턴하는게 2개의 row인데 한개만 들어감..이건 sp실행결과는 output을 받아서
# # output값을 select해서 그 값을 조회하는 방식...
# # sp에는 반드시 set nocount on을 해야만 동작한다.
# # .net에서 사용하는 방식과는 틀림
# print(rc, type(rc))
# rows = cursor.fetchall()
# print(rows, type(rows))
# for row in rows:
#     print(row.Std_No, row.Name, row.Age, row.Sex, row.LastChngDt )



# sql = """\
# DECLARE @RC int;
# EXEC dbo.sp_call_test02 @RC OUTPUT, @id_=?, @pw=?, @depart=?, @class_=?, @name=?, @birthday=?, @grade=?, @subgrade=?;
# SELECT @RC AS rc;
# """
# values = (id_, pw, depart, class_, name, birthday, grade, subgrade)
# cursor.execute(sql, values)
# rc = cursor.fetchval()

# connection을 종료한다.
conn.close();
