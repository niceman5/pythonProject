import csv
from pathlib import Path

root_dir = Path('C:\\')
file_dir = root_dir / '00.Dev' / 'study' / 'Python' / '00.LibExample' / 'file'
csv_file  = file_dir / 'sample.csv'

if csv_file.exists():
    print(csv_file, '있음')

with open(csv_file, mode='r') as f:
    # 자료형을 리스트임 .....
    reader = csv.reader(f)
    for row in reader:
        print(row)


# csv파일을 읽어서 tsv으로 기록
with open(csv_file, mode='r') as f:
    reader = csv.reader(f)
    # 한줄을 건너 뛰어서.....헤더를 날린다.
    next(reader)

    tsv_file = file_dir / 'sample.tsv'
    with open(tsv_file, mode='w', encoding='utf-8') as w_f:
        writer = csv.writer(w_f, delimiter='\t')

        #헤더 행 쓰기
        writer.writerow(['도도부현','인구밀도(km2)'])

        for row in reader:
            pop_density = float(row[2])/ float(row[3])
            writer.writerow([row[1], int(pop_density)])


with open(csv_file, mode='r') as f:
    # dict형태로 파일을 읽음.
    for row in csv.DictReader(f):
        print(row)
        # 사전형태로 읽으면 더 쉽게 사용 가능함
        print(row['id'], row['인구(명)'])