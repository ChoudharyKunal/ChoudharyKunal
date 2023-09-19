import smtplib #simple mail tranfer protocol data

my_mail = "choudharykunal474@gmail.com"
passcode="jnhdldttiwnelmfv"
to_mail = ""

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()#tranfer layer security

connection.login(user=my_mail, password=passcode)


mail_content = "Subject: this is sample subject mail \n\n this is sample mail for testing"

try:
    connection.sendmail(from_addr=my_mail,to_addrs=to_mail, msg=mail_content)
except Exception as e:
    print("something went wrong in sending mail", e)

connection.close()
