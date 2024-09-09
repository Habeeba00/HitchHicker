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
        # Establish a connection to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()  # Identify yourself to the server
            s.starttls()  # Upgrade the connection to a secure encrypted TLS connection
            s.ehlo()  # Re-identify yourself as an encrypted connection

            # Login to the SMTP server
            s.login('habibamohamed2222009u665@gmail.com', 'Habiba@01019742210')  # Replace with your actual email password

            # Send the email
            s.send_message(msg)
        
        print('Email sent successfully!')

    except Exception as e:
        print(f'Failed to send email: {e}')