import art
import random
import game_data
from replit import clear
score = 0
score1 = 0
def header():
  if score1 == 0:
    hd = f"You're right! Current score: {score}."
    return hd
  elif score1 > 0:
    hd = f"You're wrong! Current score: {score}."
    return hd


decii = "" 
stat = True
while stat:    
  the_winner = ""
  pick1 = random.choice(game_data.data)
  pick2 = random.choice(game_data.data)
  clear()  
  print(pick1['follower_count'])
  print(pick2['follower_count'])
  print(art.logo)
  if score > 0:
   print(header())
      
    
  print(f"Compare A: {pick1['name']}, a {pick1['description']}, from {pick1['country']}.")
    
  print(art.vs)
    
  print(f"Compare B: {pick2['name']}, a {pick2['description']}, from {pick1['country']}.")
    
  decision = input("Who has more followers? Type 'A' or 'B': ") .lower()
      
  if pick1['follower_count'] > pick2['follower_count']:
    the_winner = "a"
  elif pick2['follower_count'] > pick1['follower_count']:
    the_winner = "b"
        
  if decision == the_winner:
    score += 1
    score1 += 1
    score1 -= 1
  elif decision != the_winner:
    score1 += 1
   
  decii += decision
  
  if decision != the_winner or pick1['name'] == pick2['name']:
    stat = False
    clear()
    print(art.logo)
    print(header())
