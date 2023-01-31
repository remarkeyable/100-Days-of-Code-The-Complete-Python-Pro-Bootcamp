import random
import wd
import st

chosen_word = random.choice(wd.word_list)

display = []
gh = "_"
ch = len(chosen_word)
op = int(ch)
empty =""

for mm in range(ch):  
  display += gh 

disp2 = []
for bb in chosen_word:
  disp2.append(bb)  
  
count = 6  

while not display == disp2:
  guess = input("\nGuess a letter: ").lower() 
  for pos in range(ch): 
    letah = chosen_word[pos]
    if letah == guess:
      display[pos] = letah
  if guess not in display:
    count = count - 1 
  print(st.stages[count]) 
  if count == 0:
    print("YOU LOSE!") 
    break
  print(f"\n{' '.join(display)}")    
else:
  print("Ikaw na! Dabest ka!")
