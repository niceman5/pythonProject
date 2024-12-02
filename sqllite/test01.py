# 80라인에 세로선 설정 https://director-joe.kr/92 참조
import sqlite3
from enum import Enum


class Dessert(Enum):
    ID = 0
    name = 1
    kal = 2


# Decorator
def constant(func):
    def func_set(self, value):
        raise TypeError

    def func_get(self):
        return func()
    return property(func_get, func_set)


class _Dessert():
    @constant
    def ID():
        return 0

    @constant
    def NAME():
        return 1

    @constant
    def KAL():
        return 2


# 메모리에다가 DB서버를 구성(연결)하기
con = sqlite3.connect(':memory:')

# sql문 작성하고 실행할 수 있는 메모리 영역 만들기
cur = con.cursor()

cur.execute("create table dessert(id integer, name char, kal integer)")
cur.execute("insert into dessert(id,name,kal) values(1,'케이크1',324)")
cur.execute("insert into dessert(id,name,kal) values(2,'케이크2',111)")
cur.execute("insert into dessert(id,name,kal) values(3,'케이크3',33)")
# con.rollback()

cur.execute("select * from dessert")

rows = cur.fetchall()
print(rows, type(rows))
for row in rows:
    print(row, type(row))

# drink = DataFrame({'id':[1,2,3],'name' : ['콜라','사이다','커피'],'kcal': [37,44,1]})
# drink.to_sql('drink',con,index=False)
# cur.execute("select name from sqlite_master where type='table'")
# rows = cur.fetchall()
# print(rows, type(rows))
# cur.execute("PRAGMA table_info(drink)")
# cur.fetchall()
# rows = cur.fetchall()
# print(rows, type(rows))
# cur.execute("select * from drink")
# cur.fetchall()
# rows = cur.fetchall()
# print(rows, type(rows))


dessert = _Dessert()
print(dessert.ID, type(dessert.ID))
for row in cur.execute("select * from dessert"):
    print(row, type(row))   # 튜플로 
    # print(Dessert.ID, type(Dessert.ID))
    print(row[dessert.ID], type(dessert.ID))
    print(row[dessert.NAME], type(dessert.NAME))
    print(row[dessert.KAL], type(dessert.KAL))

cur.close()
con.close()


'''
# Never do this -- insecure!  이방법은 절대 사용하지 말것
symbol = 'RHAT'
cur.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead -- 이 방식을 권장한다.
t = ('RHAT',)
cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(cur.fetchone())



# Larger example that inserts many records at a time
# 한번에 다건 등록
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


# 직접쿼리를 사용할수 있음
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)


# update
# 방법 1
c.execute("UPDATE table1 SET name=? WHERE id=?", ('NEW1', 1))

# 방법 2
c.execute("UPDATE table1 SET name=:name WHERE id=:id", {"name": 'NEW2', 'id': 3})

# 방법 3
c.execute("UPDATE table1 SET name='%s' WHERE id='%s'" % ('NEW3', 5))

'''