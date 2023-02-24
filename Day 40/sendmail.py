import smtplib
import os
MY_EMAIL = os.environ["MY_EMAIL"]
PASS = os.environ["MAIL"]

class Sendmail:
    def __init__(self,mail, price,link, current_loc, to_loc):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASS)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=mail,
                                msg=f"Subject: The Current Lowest Price Deal is Here!\n\n"
                                    f"Hello~ Flight Club member. We found a great deal for you. A flight from {current_loc} to {to_loc}, "
                                    f"{price} euro only. Hurry & Checkout this link --> {link}")