from replit import clear


def morse_code(text):
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
             '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': " "}
    key = text
    #will check if text input is on the morse dictionary, if none it'll return none
    if key not in morse:
        pass
    else:
        result = morse[key]
        return result

on = True
while on:
    the_text = list(input("Type the words you want to convert: ").upper())
    #will itterate each letters from the_text list, "None" will be excluded
    the_morse = [(f" {morse_code(i)}") for i in the_text if i != " None"]
    result = [i for i in the_morse if i != " None"]
    #result list will be joined and properly format as words
    print("".join(result))
    cont = input("Do you want to convert another text? Y/N : ").upper()
    if cont == "N":
        on = False
    elif cont == "Y":
        clear()
    else:
        print('Wrong input, program exit.')
        on = False
