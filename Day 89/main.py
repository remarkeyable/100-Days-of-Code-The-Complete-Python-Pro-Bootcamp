import customtkinter
import tkinter as tk
import time
import keyboard
from pynput import keyboard

window = customtkinter.CTk()
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.title('Disappearing Text')

sec = ""


def countdown(seconds):
    global sec
    if seconds >= 0:
        sec = seconds
        print(sec)
        window.after(1000, countdown, seconds - 1)  # Schedule the next countdown after 1000 milliseconds (1 second)
    else:
        print("Countdown complete!")


# countdown(10)
def is_typing():
    global input_var
    if input_var == user_input.get(1.0, 'end-1c'):
        window.after(10000, lambda: user_input.delete("1.0", 'end'))
        # window.after(10000, lambda: print(
        #     'hello'))  # window.after(5000, lambda: countdown(  #     5))  # countdown(5)  # label_timer.configure(text=f"Your text will disappear in {time.sleep(2)}")
    else:
        print("User is typing.")
    input_var = user_input.get(1.0, 'end-1c')
    window.after(1000, is_typing)


input_var = ""
user_input = customtkinter.CTkTextbox(window, width=450, height=450, fg_color="#F4EEE0", corner_radius=0,
                                      font=('Arial', 20), text_color="#454545")
user_input.focus_set()
user_input.place(x=25, y=60)
label_timer = customtkinter.CTkLabel(window, text="Your text will disappear in")
label_timer.place(x=0)

is_typing()

window.mainloop()
