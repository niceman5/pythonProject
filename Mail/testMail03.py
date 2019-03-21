import os
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders



import time
import datetime

gmail_user="kth@u-crm.com"
gmail_pwd="gustnr35"


def send_gmail(to, subject, text, html, attach):
    msg = MIMEMultipart('alternative')
    msg['From'] = gmail_user  # <-- 발신자 이름을 바꾸려면 수정하세요. 안적으시면 메일계정이름으로 날아갑니다.
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    # managing attachment
    # 이하 주석처리된 부분이 메일 첨부파일 발송을 위한 부분입니다. 첨부파일이 필요하시면 수정해서 쓰세요.
    # part=MIMEBase('application','octet-stream')
    # part.set_payload(open(attach, 'rb').read())
    # Encoders.encode_base64(part)
    # part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
    # msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()


def mainLoop():
    title = "메일제목을 쓰세요."
    # attach_file="send_mail.py"  <--------- 첨부파일 명입니다. 없으면 그대로 주석처리 해두세요.

    # f = open("text.txt", "r")  # <------ 메일 내용의 Text버전이 들어있는 파일입니다.
    # message = f.read()
    # f.close()
    message = "메일 테스트 입니다."

    # f = open("html.html", "r")  # <------ 메일 내용의 HTML버전이 들어있는 파일입니다.
    # html = f.read()
    # f.close()
    html = ""

    print("Program Ready")
    print("----------------------")

    f = open("list.txt", "r")  # <---- 엔터키로 구분된 메일링 리스트입니다. 메일 주소가 한줄에 하나씩 있어야 합니다.
    emails = f.readlines()
    for email in emails:
        email = email.strip('\r')
        email = email.strip('\n')
        email = email.strip(' ')
        email = email.strip('\t')
        if email == "":
            continue
        print("[" + str(datetime.datetime.now()) + "] Sending email to " + email + "...")
        send_gmail(email, title, message, html, "")
        print("[" + str(datetime.datetime.now()) + "] Complete... Waiting for 5 seconds.")
        # 5초마다 보냅니다.
        time.sleep(5)
    print("Mails have just sent. The program is going to end.")

# mail.py파일을 만드시고 위 내용을 적으신 후에,
# text.txt, html.html, list.txt파일이 같은 폴더에 있어야 합니다.
# text.txt파일과 html.html파일에 메일내용이
# (각각 text버전과 html버전의 메일을 작성하셔서 파일 만드시면 됩니다)
# list.txt파일에 메일링 리스트가 있으면 됩니다.
# list.txt에 보낼 메일주소를 한 줄에 하나씩 넣어두시면 됩니다.
if __name__ == "__main__":
    mainLoop()
