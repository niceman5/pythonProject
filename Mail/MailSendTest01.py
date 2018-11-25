'''

'''

import smtplib
from email.mime.text import MIMEText


# send_mail 함수에 구현하겠습니다.
def send_mail():
    # 메일 내용을 담을 문자열을 선언합니다.
    text = 'test message'

    # smtp 인스턴스를 만들어줍니다.
    # 인자값으로는 smtp 서버 url과 port가 들어갑니다.
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # 초기에 서버와 handshaking 을 시도합니다.
    smtp.ehlo()
    # TLS를 이용해서 암호화할 것이므로 start tls 함수를 호출합니다.
    smtp.starttls()

    # smtp 서버 로그인을 위해 id 와 password를 인자로 하여 login 함수를 호출합니다.
    # id는 @가 들어간 email형식으로 입력합니다.
    smtp.login('kth@u-crm.com' 'gustnr35!')

    # MIMEText 인스턴스에는 보내려는 메일 내용을 인자값으로 넣어줍니다.
    message = MIMEText(text.encode())

    # 메일 제목은 Subject, 보내는 사람은 From, 받을 사람 정보는 To로 설정합니다.
    message['Subject'] = 'mail subject-TEST'
    message['From'] = 'kth@u-crm.com'
    message['To'] = 'niceman555@gmail.com'

    # smtp sendmail 함수를 이용하여 실제로 메일을 발송해줍니다.
    smtp.sendmail('kth@u-crm.com', 'niceman555@gmail.com', message.as_string())

    # smtp quit 함수로 인스턴스를 종료시킵니다.
    smtp.quit()



#
# 메인 프로세스 시작
#
if __name__ == '__main__':

    send_mail()