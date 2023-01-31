import random
from replit import clear
from art import logo
comp = []
user = []
def dcard():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  rand = random.choice(cards)
  return rand

def comps():
  compscore = int(sum(comp))
  return compscore
def users():
  userscore = int(sum(user))
  return userscore


def comparison():
  status = ''
  if comps() > 21:
    status = "comp lose"
  elif comps() == users():
    status = "It's a tie"
  elif comps() > users():
    status = "comp win"
  elif comps() < users():
    status = "user win"
  return status  

def score():
  stat = ""
  total = 0
  for i in comp:
    total += i
       
  if "11" and "10" in user:
    total = 0
  if "11" in user:
    if total > 21:
      comp.remove(11)
      comp.append(1)
  total1 = 0
  
  for j in user:
    total1 += j
  if "11" and "10" in user:
    total1 = 0
  if "11" in user:
    if total > 21:
      user.remove(11)
      user.append(1)
  
  if total == 0:
    stat = "user black jack"
  else:
    stat = "no winner"  
  if total1 == 0:
    stat = "comp black jack"
  else: 
    stat = "no winner"  
  
  if users() > 21:
    stat = "comp black jack"
  if users() == 21:
    stat = "user black jack"  
  return stat 



def all():
    comp.append(dcard())
    comp.append(dcard())
    user.append(dcard())
    user.append(dcard())
    print(logo)
    if score() == "user black jack":
      print(f"Your final hand: {user}, final score: {users()} ")
      print(f"Computer's final hand: {comp}, final score: {comps()}")
      print("You Win")  
    elif score() == "comp black jack":
      print(f"Your final hand: {user}, final score: {users()} ")
      print(f"Computer's final hand: {comp}, final score: {comps()}")
      print("You lose") 
    elif score() == "no winner":
      print(f"Your cards: {user}, current score: {users()}")
      print(f"Computer's first card: {comp[0]}")
    dec1 = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if dec1 == "y":
      comp.append(dcard())
      user.append(dcard())
      score()      
      if score() == "user black jack":
        print(f"Your final hand: {user}, final score: {comps()} ")
        print(f"Computer's final hand: {comp}, final score: {comps()}")
        print("You Win!")        
      elif score() == "comp black jack":
        print(f"Your final hand: {user}, final score: {users()}")
        print(f"Computer's final hand: {comp}, final score: {comps()}")
        print("You lose")
        
      elif score() == "no winner":
        print(f"Your cards: {user}, current score: {users()}")
        print(f"Computer's first card: {comp[0]}")  
      
    if dec1 == "n":
      if comparison() == "comp lose":
        print(f"Your final hand: {user}, final score: {users()} ")
        print(f"Computer's final hand: {comp}, final score: {comps()}")
        print("You Win!")  
      elif comparison() == "comp win":
        print(f"Your final hand: {user}, final score: {users()} ")
        print(f"Computer's final hand: {comp}, final score: {comps()}")
        print("You Lose!")
      elif comparison() == "user win":
        print(f"Your final hand: {user}, final score: {users()} ")
        print(f"Computer's final hand: {comp}, final score: {comps()}")
        print("You win!")
      
      elif comparison() == "It's a tie":
        print(f"Your cards: {user}, current score: {users()}")
        print(f"Computer's first card: {comp[0]}")
        print("It's a tie!")
      
  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  comp.clear()
  user.clear()
  all()
