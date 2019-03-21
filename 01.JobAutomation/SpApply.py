import pyodbc
import os
import sys


#
# Main Process 처리
#
if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('적용할 db서버[test, dev, real], sp목록파일명을 입력하세요.')
        sys.exit(1)

    db_serv = sys.argv[1].lower()
    out_file = sys.argv[2].lower()

    # db_serv = 'dev'
    # out_file = 'output.txt'

    conn = None

    if db_serv == 'test':
        conn = pyodbc.connect(
            '')
    elif db_serv == 'dev':
        conn = pyodbc.connect(
            '')
    elif db_serv == 'real':
        conn = pyodbc.connect(
            '')
    else:
        sys.exit(1)

    cursor = conn.cursor()

    with open(out_file, 'r', encoding='utf-8') as out:
        for file_name in out.readlines():
            file_name = file_name.strip()  #공백을 제거한다.

            # 주석이나 공백라인은 skip한다.
            if file_name.startswith('#') or len(file_name) == 0:
                continue
            
            # 인코딩 타입이 유니코드(unicode) 또는 UTF-8인 문서를 읽을 때 파일의 처음에 \ufeff 가 추가되는데,
            # \ufeff문서의시작
            # 그래서 파일을 읽을때 아예 옵션을 주고 읽으면 제거하고 읽는다.
            # utf-8-sig 인코딩을 utf-8로 하면서 BOM(Byte Order Mark)을 없앤다

            print(file_name, end='')

            # execute로 실행시 GO문때문에 오류 남으로 GO를 기준으로 sp를 나눠서 실행시킨다.
            # 파일을 읽을때 코드문제는 무시하는 방식으로 open
            with open(file_name, 'r', encoding='utf-8-sig', errors='ignore') as sp:
                sp_lines = sp.readlines()
                sp_full = ''
                # print (sp_lines)
                for sp_line in sp_lines:
                    # 문자의 라인에 GO만 있으면
                    if sp_line.strip().lower() == 'go':
                        sp_line2 = 'GO'
                    
                    #문장의 오른쪽 공백을 없애고 sp를 만든다.
                    sp_full = sp_full + sp_line.rstrip()+'\n'

                #print(sp_full)
                sp_txts = sp_full.split('GO\n')

                for part_sp_txt in sp_txts:                    
                    if len(part_sp_txt) > 0:
                        # print(part_sp_txt)
                        cursor.execute(part_sp_txt)
            print('---->적용')

            conn.commit()

            #    sp_txt = sp.read().strip()
            #    print(file_name)
            #    sp_txts = sp_txt.split('GO\n')                
            #    for part_sp_txt in sp_txts:                    
            #        if len(part_sp_txt) > 0:
            #            print(part_sp_txt)
            #            cursor.execute(part_sp_txt)
            #conn.commit()

