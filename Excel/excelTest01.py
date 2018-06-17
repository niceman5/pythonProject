# pip install openpyxl
# excel을 사용할수 있는 라이브러리

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active         # 현재 열린 sheel를 설정한다.
ws1.title = '첫번째 Sheet'
ws1["A1"] = "Hello World!!!"
wb.save("sample.xlsx")

