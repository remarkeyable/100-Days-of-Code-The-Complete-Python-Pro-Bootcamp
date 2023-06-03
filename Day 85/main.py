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
    global chosen_word, entry, word_counts
    if chosen_word == entry.get() + event.char:
        entry.delete(0, 'end')
        window.after(100, lambda: entry.delete(0, 'end'))
        word_counts += 1
        print(time_time)
        generate_word()
        words.configure(text=chosen_word)


import time


def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time remaining: {remaining_time} seconds")
        time.sleep(1)

    print("Time's up!")


# Example usage: Set the timer for 10 seconds
timer(10)


def generate_word():
    global chosen_word
    with open('words.csv') as text:
        words = list(text)
        chosen_word = random.choice(words).strip()


def timer():
    global time_time
    time_time = time.time()



generate_word()
words = customtkinter.CTkLabel(window, text=chosen_word)
words.pack()

label = customtkinter.CTkLabel(window, text="")
label.pack()

entry = customtkinter.CTkEntry(window)
entry.pack()

start_t = customtkinter.CTkButton(window, text="start", command=timer)
start_t.pack()
entry.focus()
entry.bind("<Key>", start)



window.mainloop()
