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
trigger = False


def countdown():
    global sec
    for i in range(5, -1, -1):
        time.sleep(1)
        label_timer.configure(text=f"Your text will disappear in {i}")
        if pause:
            break


def is_typing(event):
    global pause, trigger
    pause = True
    trigger = False
    print("typing")


def is_not_typing(event):
    global trigger
    trigger = True
    j = window.after(10000, lambda: user_input.delete("1.0", 'end'))
    i = window.after(5000, lambda: print("hello"))

    if trigger is True:
        window.after_cancel(j)


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
