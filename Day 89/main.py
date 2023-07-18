import customtkinter
import tkinter as tk
import time

window = customtkinter.CTk()
window.minsize(width=550, height=550)
window.maxsize(width=550, height=550)
window.title('Disappearing Text')

sec = 0
pause = False
after_id = None


def countdown():
    global sec, after_id
    for i in range(5, -1, -1):
        label_timer.configure(text=f"Your text will disappear in {i}")
        window.update()
        if pause:
            break
        window.after(1000)
    if not pause:
        user_input.delete("1.0", 'end')
    after_id = None


def is_typing(event):
    global pause, after_id
    label_timer.configure(text=f"Nice, you're typing")
    if after_id:
        window.after_cancel(after_id)


def is_not_typing(event):
    global after_id
    if after_id:
        window.after_cancel(after_id)
    after_id = window.after(5000, countdown)


input_var = customtkinter.StringVar()
user_input = customtkinter.CTkTextbox(window, width=500, height=450, fg_color="transparent", corner_radius=0,
                                      font=('Arial', 18), text_color="#454545", border_width=2)
user_input.focus_set()
user_input.place(x=25, y=60)
label_timer = customtkinter.CTkLabel(window, text="Start Typing", font=('Arial', 20), text_color="#454545")
label_timer.place(x=30, y=20)

window.bind("<KeyPress>", is_typing)
window.bind("<KeyRelease>", is_not_typing)

window.mainloop()
