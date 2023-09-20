import smtplib #simple mail tranfer protocol data
from  email.message import EmailMessage
import ssl

#setting up port and server name

smtp_port = 587
smtp_server = "smtp.gmail.com"

#setting up
my_mail = "choudharykunal474@gmail.com"
passcode="jnhdldttiwnelmfv"
to_mail = "baisoyakunal69@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()#tranfer layer security

#connection.login(user=my_mail, password=passcode)


message = "Please find attached report for todays stock data"
mail_content = ssl.create_default_context()



#mail_content['Subject'] = "Stock Report for today"
#mail_content["From"] = my_mail
#mail_content["To"] = to_mail



try:

    print("connecting to server")
    TIE_server = smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.starttls(context=mail_content)
    TIE_server.login(my_mail,passcode)
    print("connect to server")
    print()

    print(f"Sending  email to -{to_mail}")

    TIE_server.sendmail(my_mail,to_mail,message)
    print(f"Successfully  email sent to -{to_mail}")
except Exception as e:
    print(e)



finally:

    TIE_server.close()
