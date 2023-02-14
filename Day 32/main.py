
import smtplib
from datetime import datetime
import pandas
import random

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
with open("./letter_templates/letter_1.txt") as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", "Ryn")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login("", "")
        connection.sendmail(
            from_addr="",
            to_addrs="",
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
