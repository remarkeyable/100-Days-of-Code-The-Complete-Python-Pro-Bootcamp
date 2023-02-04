
# My first code
# list_of_names = ["Aang", "Zuko", "Appa", "Katara", "Sokka", "Momo", "Uncle Iroh", "Toph"]
# letter = open("./Input/Letters/starting_letter.txt")
# reading = letter.read()
# for names in list_of_names:
#   fn = open(f"./Output/ReadyToSend/{names}.txt", "x")
#   fn.write(reading)
# for names in list_of_names:
#   i = open(f"./Output/ReadyToSend/{names}.txt", "r")
#   j = i.read()
#   k = j.replace("[name]", f"{names}")
#   i.close()
#   l = open(f"./Output/ReadyToSend/{names}.txt", "w")
#   l.write(k)

#changed my codes:

with open("./Input/Names/invited_names.txt") as names:
  list = names.readlines()
with open("./Input/Letters/starting_letter.txt") as letters:
  invitation = letters.read()
for name in list:
  remove_space = name.strip()
  with_names = invitation.replace("[name]", f"{remove_space}")
  with open(f"./Output/ReadyToSend/Dear {remove_space}", "w") as generate_files:
    generate_files.write(with_names)
















