import pymssql
import json

lst_data = [
{'SOLA_DA': '2024-01-01', 'LUNA_DA': '2023-11-20', 'LEAP_YEAR_TXT': '윤', 'LEAP_MON_TXT': '평', 'WEEK_NM': '월', 'GANJI': '계묘(癸卯)'},
{'SOLA_DA': '2024-01-02', 'LUNA_DA': '2023-11-21', 'LEAP_YEAR_TXT': '윤', 'LEAP_MON_TXT': '평', 'WEEK_NM': '화', 'GANJI': '계묘(癸卯)'}
]

# print(lst_data)
json_str = json.dumps(lst_data, ensure_ascii=False)

# mssql
conn = pymssql.connect(host=r"220.95.213.77", user="upds_adm",
                       password="ucrm027194300!", database="UBIS")


with conn.cursor(as_dict=True) as cursor:
    res = cursor.callproc('COM.dbo.upCOM_PUBL_SOLA_LUNA_UPDATE', (json_str,pymssql.output(int),pymssql.output(str)) )
    conn.commit()

print(res[len(res)-2])      # output건수
print(res[len(res)-1])      # output메시지
conn.close()