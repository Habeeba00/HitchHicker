import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email,subject,body):
    msg=MIMEMultipart()
    msg['From']="habibamohamed2222009u665@gmail.com"
    msg["To"]=to_email
    msg['Subject']=subject
    body=body
    msg.attach(MIMEText(body,"plain"))


    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo() 
            s.starttls()
            s.ehlo()

            s.login('habibamohamed2222009u665@gmail.com', 'Habiba@12345')  # Replace with your actual email password

            s.send_message(msg)
        
        print('Email sent successfully!')

    except Exception as e:
        print(f'Failed to send email: {e}')