from data import Data
import smtplib
import pandas

data = Data()
cur_loc = input("Where is your current location? : ")
fly_to = input("Where do you want to travel? : ")
date_from = input("Date from? : ")
date_to = input("Date to? : ")
night_dst = input("Nights in destination? : ")
cur_loc1 = data.iata(cur_loc)
fly_to1 = data.iata(fly_to)

data.search(cur_loc1,fly_to1,date_from,date_to,night_dst)



