import json
import boto3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# Initialize S3 and SMTP clients
s3_client = boto3.client('s3')
smtp_port = 587
smtp_server = "smtp.gmail.com"
my_mail = "choudharykunal474@gmail.com"
passcode = "jnhdldttiwnelmfv"
email_list = ["baisoyakunal69@gmail.com", "choudharykunal474@gmail.com"]

def lambda_handler(event, context):
    try:
        # Set up S3 resource
        s3 = boto3.resource('s3')

        # Create the filename
        latest_filename = filename_create()
        
        # Download the file from S3
        s3.meta.client.download_file('dailystockreportdata', 'StockReport-092023.csv', f'/tmp/{latest_filename}')
        print(f"File downloaded successfully: {latest_filename}")

        # Send emails to recipients
        send_emails(email_list, latest_filename)
        print("Data sent")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def filename_create():
    now = datetime.now()
    month_date_year = now.strftime("%m%d%y")
    filename = f'StockReport-{month_date_year}.csv'
    return filename

def send_emails(email_list, latest_filename):
    try:
        for person in email_list:
            subject = f"Daily Stock Data Report for {latest_filename}"
            
            # Email body
            body = f"""
            Hi Subscriber,
            
            Please find today's stock data report attached below as {latest_filename}. 
            
            Thanks and Regards,
            The Stock Reporter
            """

            # Create a MIME object to define parts of the email
            msg = MIMEMultipart()
            msg["From"] = my_mail
            msg["To"] = person
            msg["Subject"] = subject

            # Attach the body of the message
            msg.attach(MIMEText(body, 'plain'))

            # Open and encode the file as base64
            with open(f'/tmp/{latest_filename}', 'rb') as attachment:
                attachment_package = MIMEBase('application', 'octet-stream')
                attachment_package.set_payload(attachment.read())
                encoders.encode_base64(attachment_package)
                attachment_package.add_header('Content-Disposition', f'attachment; filename={latest_filename}')
                msg.attach(attachment_package)

            # Convert message to string
            text = msg.as_string()

            # Connect to the SMTP server
            print("Connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(my_mail, passcode)
            print("Connected to server")

            # Sending email to person
            print(f"Sending email to: {person}")
            TIE_server.sendmail(my_mail, person, text)
            print(f"Successfully sent email to: {person}")

        TIE_server.quit()
    except Exception as e:
        print(f"An error occurred while sending emails: {str(e)}")

