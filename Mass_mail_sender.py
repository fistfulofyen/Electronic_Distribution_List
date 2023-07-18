from email.message import EmailMessage
import ssl
import smtplib
import re
import pandas as pd


def validate_enail(email_list):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    #add our examples email to a list
    invalid = False
    for email in email_list :
        #match the email and regex
        if(re.fullmatch(regex, email)):
            
            print(email,"  : Valid")

        else:
            
            print(email," : InValid")
            invalid == True

    if invalid:
        exit()
        

def get_email_list_from_csv(csv_path):
    data = pd.read_csv(csv_path)
    email_list = data['EMAIL_ADDR']
    return email_list


if __name__ == '__main__':
    sender = "sender_email_account@gmail.com"
    password = 'app_password'

    # email_list = [
    # 'gsmith123@example.com',
    # 'jdoe456@example.com',
    # 'lwilliams789@example.com',
    # 'akim321@example.com',
    # 'bharris654@example.com'
    # ]

    email_list = get_email_list_from_csv('EMAIL_ADDRES_VW.csv')

    receiver = email_list
    carbon_copy = ''
    subject_line = 'This is the subject ofthe email'
    body = '''
        This is the body of the email

    '''

    email = EmailMessage()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject_line
    email.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender,password )
        smtp.sendmail(sender,receiver,email.as_string())
