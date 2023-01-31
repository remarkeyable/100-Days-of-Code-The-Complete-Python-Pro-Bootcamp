print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lower = name1.lower()
lower2 = name2.lower()
combi = lower + lower2

t = int(combi.count("t"))
r = int(combi.count("r"))
u = int(combi.count("u"))
e = int(combi.count("e"))
l = int(combi.count("l"))
o = int(combi.count("o"))
v = int(combi.count("v"))
e = int(combi.count("e"))

total1 = str(t + r + u + e)
total2 = str(l + o + v + e)
total3 = (total1 + total2)
final = int(total3)


if final < 10 or final > 90:
 print(f"Your score is {final}, you go together like coke and mentos.")
elif final >= 40 and final <= 50:
 print(f"Your score is {final}, you are alright together.")
else:
 print(f"Your score is {final}.")
