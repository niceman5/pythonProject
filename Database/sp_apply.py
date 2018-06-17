
import os
import sys
import pyodbc

#
# Main Process 처리
#
if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('적용할 db서버[test, dev, real] 적용할 file명')
        sys.exit(1)

    db_serv = sys.argv[1]
    out_file = sys.argv[2]

    # conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=TEST;UID=niceman5;PWD=gustnr35!')
    # cursor = conn.cursor()

    with open(out_file, 'r', encoding='utf-8') as out:
        for file_name in out.readlines():
            file_name = file_name.strip()  # 공백을 제거한다.

            # 주석이나 공백라인은 sklip한다.
            if file_name.startswith('#') or len(file_name) == 0:
                continue

            with open(file_name, 'r', encoding='utf-8') as sp:
                sp_txt = sp.read()
                print(sp_txt)
                #cursor.execute(sp_txt)


