import smtplib
from email.mime.text import MIMEText

def sendMail(me, you, msg):
    content = MIMEText(msg, _charset='euc-kr')
    content['Subject'] = 'TEST'
    content['From'] = me
    content['to'] = you

    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(me, 'gustnr35!')
    smtp.sendmail(me, you, content.as_string())
    smtp.quit()


#
# 메인 프로세스 시작
#
if __name__ == '__main__':
    s = '메일보내기'
    sendMail('kth@u-crm.com', 'niceman555@gmail.com', '메일보내기')