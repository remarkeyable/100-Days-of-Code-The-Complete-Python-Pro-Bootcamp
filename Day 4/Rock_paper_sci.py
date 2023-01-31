import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

pref = input("Please choose, 0 for rock, 1 for paper, 2 for scissors: ")

random1 = [rock, paper, scissors]
ran = random.choice(random1)



if pref == "0":
  print(rock,)
elif pref == "1":
   print(paper)
elif pref == "2":
  print(scissors)


print(f"Computer chose: {ran}")

if pref == "0" and ran == rock:
 print("A tie")
if pref == "0" and ran == paper:
 print("You lose")
if pref == "0" and ran == scissors:
 print("You lose")
if pref == "1" and ran == rock:
 print("You win")
if pref == "1" and ran == paper:
 print("A tie")
if pref == "1" and ran == scissors:
 print("You lose")
if pref == "2" and ran == rock:
 print("You lose")
if pref == "2" and ran == paper:
 print("You win")
if pref == "2" and ran == scissors:
 print("You lose")
