# creating two email accounts on gmail
# two email account on yahoo

# ustawic ustawienia security na mailu

import smtplib

my_email = "appbreweryinfo@gmail.com"
password = "abc1234()"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="appbrewerytesting@yahoo.com", msg="Hello")
connection.close()