import os
import sys
import csv
import pyodbc

##
# Main Process 처리
#
if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('1)csv파일명 등록할 db[test, dev, real]를 입력하세요')
        sys.exit(1)

    # 전달 받은 파일명을 분리한다
    csv_file = sys.argv[1]
    db_serv = sys.argv[2].lower()

    print(csv_file)

    atte_list = []
    json_str = ''

    conn = None

    if db_serv == 'test':
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=220.95.213.77,1436;DATABASE=ubis;UID=ubis;PWD=ubis')
    elif db_serv == 'dev':
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=220.95.213.75;DATABASE=ubis;UID=ubis;PWD=ubis')
    else:
        sys.exit(1)

    cursor = conn.cursor()


    with open(csv_file, mode='r') as f:
        rdr = csv.reader(f)
        # a = len(rdr)
        # print(type(rdr))

        # reader = csv.DictReader(f)
        # out = json.dumps([line for line in reader]);
        # print(out)

        # for line in csv.DictReader(f):
        #     print(line)
        # new_list =  list(rdr)
        # print(len(new_list))
        for line in rdr:
            # if line[0] == '' or (line[2] != '김태훈' and line[2] != '정우현'):
            if line[0] == '':
                continue
            # print(line)
            # 데이터 등록용 리스트를 구한다.....일자/이름/출근/퇴근
            atte_list.append([line[0], line[2], line[6], line[7]])
            json_str = json_str + "{" + '"date":"{}", "name":"{}", "in_time":"{}","out_time":"{}"'.format(line[0], line[2], line[6], line[7]) + "},"

        # print(len(json_str))
        json_str = "[" + json_str[0:len(json_str)-1] + "]"
        # print(json_str)

        sql = """
        DECLARE @RES int;
        EXEC UCRM_STATS.dbo.upWORKER_ATTE_Insert @ADMIN_ACNT_NO=?, @JSON_DATA=?, @RESULT = @RES OUTPUT;
        SELECT @RES AS rc;        
        """
        values = (50083, json_str)

        cursor.execute(sql, values)
        rc = cursor.fetchval()

        if rc > 0:
            conn.commit()

    # connection종료
    conn.close()

