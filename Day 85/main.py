import customtkinter
import tkinter as tk
import csv
import random
from tkinter import END
from CTkMessagebox import CTkMessagebox
import time
import pyautogui

window = customtkinter.CTk()

window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.title("Typing Speed Test")

chosen_word = ""
word_counts = 0


def start(event):
    global chosen_word, entry, word_counts, timer, label2
    if chosen_word == entry.get().upper() + event.char.upper():
        entry.delete(0, 'end')
        window.after(100, lambda: entry.delete(0, 'end'))
        word_counts += 1
        generate_word()
        words.configure(text=chosen_word)
    if entry._state == "disabled":
        label2.configure(text=f"Your Final Score: {round(word_counts * 1.5)} WMP")



def generate_word():
    global chosen_word
    with open('words.csv') as text:
        words = list(text)
        chosen_word = random.choice(words).strip().upper()


def restart():
    global entry, word_counts, label2
    entry.configure(state="normal")
    word_counts = 0
    entry.delete(0, 'end')
    window.after(10000, lambda: entry.configure(state='disabled'))
    label2.configure(text="Your Final Score")


generate_word()
words = customtkinter.CTkLabel(window, text=chosen_word, font=("Arial", 40))
words.place(relx=0.5,rely=0.3,  anchor="center")

# label = customtkinter.CTkLabel(window, text="")
# label.pack()

entry = customtkinter.CTkEntry(window, width=200,height=30)
entry.place(relx=0.5,rely=0.5,  anchor="center")


restart_t = customtkinter.CTkButton(window, text="start", command=restart)
restart_t.place(relx=0.5,rely=0.6,  anchor="center")

entry.focus()
entry.bind("<Key>", start)

label2 = customtkinter.CTkLabel(window, text="Your Final Score: ")
label2.pack()

window.mainloop()
