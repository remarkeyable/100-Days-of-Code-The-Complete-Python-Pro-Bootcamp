year = int(input("Which year do you want to check? "))
one = float(year % 4)
two = float(year % 100)
three = float(year % 400)


if one != 0.0:
  print("Not leap year.")
elif two != 0.0:
  print("Leap year.")
elif three == 0.0:
  print("Leap year.")
else:
  print("Not leap!")
