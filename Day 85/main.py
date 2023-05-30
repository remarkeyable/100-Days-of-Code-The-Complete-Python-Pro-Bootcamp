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
        global chosen_word, entry
        if chosen_word == entry.get() + event.char:
            print("hello")
            generate_word()
            entry.delete(0, END)
            words.configure(text=chosen_word)



       


def generate_word():
    global chosen_word
    with open('words.csv') as text:
        words = list(text)
        chosen_word = random.choice(words).strip()


generate_word()
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
