# 1. użycie serwisu pythonanywhere, zalozenie nowego konta, files, upload file -> csv, txt, main
# Consoles -> new bash console
# python3 main.py (w przypadku błedów, pozwolic na swojej poczcie)
# Task section -> scheduled tasks, python3 main.py - ustawic czas

import datetime as dt
import smtplib
import pandas
import random


MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abc1234()"

today = dt.datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data.row["month"], data.row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}")