from data import Data

#starting point = user will enter aita location, my plan is to automatically convert input data but I reached sheety monthly quota 
#during the process
cur_loc = input("What is your current location? :")

data = Data()
data.iata()
data.update()
data.search(cur_loc)
