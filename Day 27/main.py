from tkinter import *


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=150)
window.config(padx=10, pady=30)

label = Label(text= "Is equal to", font=("Arial", 10, "normal"))
label.grid(row=2, column=1)

input = Entry()
input.grid(row= 1, column=2)

miles = Label(text="Miles", font=("Arial", 10, "normal"))
miles.grid(row=1, column=3)

km = Label(text="Km", font=("Arial", 10, "normal"))
km.grid(row=2, column=3)

computation = Label(text="0", font=("Arial", 10, "normal"))
computation.grid(row=2, column=2)

def calculate_button():
    result = int(input.get()) * 1.60
    computation.config(text =round(result))

button = Button(text="Calculate", command=calculate_button)
button.grid(row=3, column=2)

window.mainloop()