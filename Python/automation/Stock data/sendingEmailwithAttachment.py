import smtplib #simple mail tranfer protocol data
from  email.message import EmailMessage
import ssl
from  email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#setting up port and server name

smtp_port = 587
smtp_server = "smtp.gmail.com"

#setting up
my_mail = "choudharykunal474@gmail.com"
passcode="jnhdldttiwnelmfv"
#email_list = ["baisoyakunal69@gmail.com","choudharykunal474@gmail.com"]



def send_emails(email_list,latest_filename):
    for person in email_list:
        subject = f"Daily Stock Data Report for {latest_filename}"
        #body for email
        body = f"""
        Line1
        Line2
        Line3
        etc
        """

        #making a MIME objet to define parts of the email

        msg = MIMEMultipart()
        msg["From"] = my_mail
        msg["To"] = person
        msg["Subject"] = subject

        #attach the bosy of the message
        msg.attach(MIMEText(body,'plain'))

        filename = str(latest_filename)

        attachment = open(filename,'rb')

        #encode as base 64

        attachment_package = MIMEBase('application','octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition','attachment; filename =' + filename)
        msg.attach(attachment_package)

        #cast as string
        text = msg.as_string()

        #conect to server
        print("connecting to server")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(my_mail, passcode)
        print("connect to server")
        print()

        #sending email to person
        print(f"Sending  email to -{person}")

        TIE_server.sendmail(my_mail, person, text)
        print(f"Successfully  email sent to -{person}")

    TIE_server.quit()


#send_emails(email_list)



