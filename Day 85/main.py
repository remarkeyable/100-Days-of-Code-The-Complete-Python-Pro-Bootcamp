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
    window.after(20000,lambda : entry.configure(state='disabled'))
    if chosen_word == entry.get() + event.char:
        entry.delete(0, 'end')
        window.after(100, lambda: entry.delete(0, 'end'))
        word_counts += 1
        generate_word()
        words.configure(text=chosen_word)

def generate_word():
    global chosen_word
    with open('words.csv') as text:
        words = list(text)
        chosen_word = random.choice(words).strip()






generate_word()
words = customtkinter.CTkLabel(window, text=chosen_word)
words.pack()

label = customtkinter.CTkLabel(window, text="")
label.pack()

entry = customtkinter.CTkEntry(window)
entry.pack()

start_t = customtkinter.CTkButton(window, text="restart")
start_t.pack()
entry.focus()
entry.bind("<Key>", start)

label2 = customtkinter.CTkLabel(window, text="hello")
label2.pack()

window.mainloop()
