import customtkinter
import csv
import random
from tkinter import END
from CTkMessagebox import CTkMessagebox
import time


window = customtkinter.CTk()


window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.title("Typing Speed Test")



chosen_word = ""
def start(event):
        # print(chosen_word)
        # print(len(chosen_word) -1)
        # print(len(entry.get() + event.char))
        if len(chosen_word) -1  < len(entry.get() + event.char):
            print(entry.get() + event.char)
            if chosen_word != str(entry.get() + event.char):
                words.configure(fg_color="#CD1818")
            else:
            # elif chosen_word == str(entry.get() + event.char):
                print("yesy")
                generate_word()
                words.configure(text= chosen_word)
        elif chosen_word == str(entry.get()):
            print("yesy")
        # else:
        #     words.configure(fg_color="transparent")


def generate_word():
    global chosen_word
    with open('words.csv') as text:
        choice = random.choice(list(text))
        chosen_word = choice

generate_word()
    # if text != entry.get():
    #     print(entry.get() + event.char)
    #     label.configure(text= event.char, text_color="#B70404")
    # else:
    #     label.configure(text=entry.get(), text_color="#27374D")

    # label.configure(text= entry.get())


text = "hello"

words = customtkinter.CTkLabel(window,text=chosen_word)
words.pack()

label = customtkinter.CTkLabel(window, text="")
label.pack()

entry = customtkinter.CTkEntry(window)
entry.pack()

start_t = customtkinter.CTkButton(window, text="start",command=start)
start_t.pack()

entry.bind("<Key>",start)








window.mainloop()
