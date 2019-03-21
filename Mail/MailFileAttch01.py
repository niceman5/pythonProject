import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import io

def email_sup_teams(team_name, contact_list, file_attachemnt):
    message_list = []
    for jobs in file_attachemnt:
        for k, v in jobs.items():
            message_list.append(v + ',')
    attachment_text = "\n".join(message_list)
    print(type(attachment_text))
    # Create the container (outer) email message.
    msg = MIMEMultipart()
    #msg = MIMEText(' Failed jobs list. Please see attachment')
    msg['Subject'] = 'Not run Jobs for ' + team_name
    msg['From'] = 'a@b.com'
    msg['To'] = 'c@d.com'
    msg.preamble = 'Failed jobs list. Please see attachment'
    f = io.StringIO(attachment_text)
    attachment = MIMEText(f.getvalue())
    attachment.add_header('Content-Disposition', 'attachment', filename='jobs_not_run.xls')
    msg.attach(attachment)

    s = smtplib.SMTP('smlsmtp')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    print('\n' + team_name + ' Email Sent')

#
# 메인 프로세스 시작
#
if __name__ == '__main__':
    email_sup_teams()