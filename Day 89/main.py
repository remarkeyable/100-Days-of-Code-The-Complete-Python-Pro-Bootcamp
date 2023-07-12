import customtkinter
import time
import keyboard
from pynput import keyboard

window = customtkinter.CTk()
window.minsize(width=400, height=400)
window.maxsize(width=400, height=400)
window.title('Disappearing Text')


input = customtkinter.CTkTextbox(window, width=200, height=250)
input.pack()

window.mainloop()
