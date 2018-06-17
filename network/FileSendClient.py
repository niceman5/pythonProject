import socket
import sys

HOST = 'localhost'
PORT = 9009

# 클라이언트 측의 파일을 서버로 전송한다.

def TcpFileSend(filename):
    data_transferred = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(filename.encode())

        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' % filename)
            return

        with open('download/' + filename, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)

    print('파일[%s] 전송종료. 전송량 [%d]' % (filename, data_transferred))


#
# main 프로세스 시작
# 특정파일들의 목록파일을 받아서 전송한다.
#
if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('업로드할 목록파일을 입력하세요.')
        sys.exit(1)

    # 목록파일
    out_file = sys.argv[1]

    with open(out_file, 'r', encoding='utf-8') as out:
        for file_name in out.readlines():
            file_name = file_name.strip()  # 공백을 제거한다.
            # 주석이나 공백라인은 sklip한다.
            if file_name.startswith('#') or len(file_name) == 0:
                continue

            TcpFileSend(filename)

