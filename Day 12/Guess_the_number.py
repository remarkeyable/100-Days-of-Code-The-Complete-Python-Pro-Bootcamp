import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dec = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

lives = 0
if dec == "easy":
  lives = 5
elif dec == "hard":
  lives = 10 
pick = random.randint(1, 100)
   
def track(gueshh):
  if gueshh > pick:
    res = "Too high"
  elif gueshh < pick:
    res = "Too low"
  elif gueshh == pick:
    res = f"Amacana, Accla! The answer was {pick}."
  return res  
    
if dec == "easy":
  print(f"You have {lives} attempts remaining to guess the number.")
  guesh = int(input("Make a guess: "))
  print(track(guesh))
  
else:
  print(f"You have {lives} attempts remaining to guess the number.")
  guesh = int(input("Make a guess: "))
  print(track(guesh))

if guesh != pick:
  lives = lives - 1
stat = True
while stat:    
  gues2 = int(input("Guess again: "))  
  if gues2 != pick:  
    lives = lives - 1  
    print(f"You have {lives} attempts remaining to guess the number.")
    print(track(gues2))
  if gues2 == pick:
    stat = False  
    print(f"Amacana, Accla! The answer was {pick}.")
  elif lives == 0:
    stat = False
    print("No remaining lives. OMG! Mhieee, You lose!")  
  
