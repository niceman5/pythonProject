import smtplib

def mail_send(gmail_user, gmail_app_password, file_name, send_to):
    print(gmail_user, file_name, send_to)
    return


if __name__ == '__main__':
    gmail_user = 'kth@u-crm.com'
    gmail_app_password = 'gustnr35!'
    file_name = 'C:\\00.Dev\Study\Python\Mail\list.txt'
    send_to = 'niceman555@gmail.com'
    mail_send(gmail_user, gmail_app_password, file_name, send_to)