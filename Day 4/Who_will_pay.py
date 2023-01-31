# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

chosen = len(names)
chosen_1 = range(chosen)
chosen_3 = random.sample(names, 1)
remove=str(chosen_3)
remove=remove.replace("[","")
remove=remove.replace("]","")
remove=remove.replace("'","")
remove=remove.replace("'","")



print(f"{remove} is going to buy the meal today!")
