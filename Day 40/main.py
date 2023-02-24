from data import Data
from ui import Ui
import pandas

data = Data()
#will convert csv into list and pass it to Ui class and Data class
with open("places.csv") as places:
    a = pandas.read_csv(places)
    b = a['Country'].tolist()

ui= Ui(b)


