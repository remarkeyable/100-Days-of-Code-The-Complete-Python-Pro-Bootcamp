import customtkinter
import tkinter as tk
import time
import keyboard
from pynput import keyboard

window = customtkinter.CTk()
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.title('Disappearing Text')

sec = 0

pause = False


def countdown():
    global sec
    time.sleep(1)
    sec = 5
    time.sleep(1)
    sec = 4
    time.sleep(1)
    sec = 3
    time.sleep(1)
    sec = 2
    time.sleep(1)
    sec = 1


def is_typing(event):
    global pause
    pause = True
    window.after_cancel(event)


def is_not_typing(event):
    window.after(10000, lambda: user_input.delete("1.0", 'end'))
    window.after(5000, lambda: label_timer.configure(text="Your text will disappear in 1"))


input_var = customtkinter.StringVar()
user_input = customtkinter.CTkTextbox(window, width=450, height=450, fg_color="#F4EEE0", corner_radius=0,
                                      font=('Arial', 20), text_color="#454545")
user_input.focus_set()
user_input.place(x=25, y=60)
label_timer = customtkinter.CTkLabel(window, text="Your text will disappear in")
label_timer.place(x=0)

# is_typing()


window.bind("<KeyPress>", is_typing)
window.bind("<KeyRelease>", is_not_typing)

window.mainloop()
