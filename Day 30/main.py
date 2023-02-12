from tkinter import *
import  customtkinter
from tkinter import messagebox
import random
import pyperclip
import json

#--------------PASSWORD_GENERATOR-------------------#

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    passhword = ""
    for char in password_list:
      passhword += char
    password.delete(0, END)
    password.insert(0,passhword)

#--------------SAVE__TEXT-------------------#

#Will save the inputs from entry text to password.json file
def save_input():
    weby = website.get()
    mail = email.get()
    the_pass = password.get()
    new_file = {
         weby: {
            "email": mail,
            "password" : the_pass

        }
    }
    if website.get() == "" or email.get() == "" or password.get() == "":
        messagebox.showinfo(title="Warning", message="All field must be filled.")
    else:
        try:
            with open("password.json","r") as data:
                file = json.load(data)
                file.update(new_file)
        except:
            with open("password.json", "w") as data2:
                json.dump(new_file, data2, indent=4)
        else:
            with open("password.json", "w") as data2:
                json.dump(file,data2, indent=4)
        finally:
            messagebox.showinfo(title="Warning", message="Saved")
            clear()
            window.focus()


#Will search on Jason file

def search():
    web = website.get()
    try:
        with open("password.json", "r") as look_up:
            file = json.load(look_up)
    except FileNotFoundError:
        messagebox.showinfo(message="No data found! ")
    else:
        if web in file:
            email = file[web]['email']
            the_password = file[web]['password']
            messagebox.showinfo(title=f"{web}", message=f"Email: {email}\n\nPassword: {the_password}")
        else:
            messagebox.showinfo(message="No data found! ")


#Will clear the entry text field when add button click
def clear():
    if website.get() != "":
        website.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)

#Will copy the password on entry
def copyy():
    pyperclip.copy(password.get())

#--------------UI_SETUP-------------------#


#Codes for window

window = Tk()
window.minsize(width=400, height=420)
window.maxsize(width=400, height=420)
window.title("Password Manager")


#Codes for canvas

image = PhotoImage(file="logo.png")
canvas = Canvas(width=300, height=300)
canvas.create_image(200, 189, image = image)
canvas.place(x=-5, y=-80)

#Codes for entry text

website = customtkinter.CTkEntry(master=window,placeholder_text="Website", corner_radius=40, width=200, border_color="#D1D1D1")
website.place(x=100, y= 200)


email = customtkinter.CTkEntry(master=window, placeholder_text="Email or Username", corner_radius=40, width=200, border_color="#D1D1D1")
email.place(x=100, y= 240)

password = customtkinter.CTkEntry(master=window, placeholder_text="Password", corner_radius=40, width=200, border_color="#D1D1D1")
password.place(x=100, y= 280)

#Codes for buttons

generate_password = customtkinter.CTkButton(master= window, text="Generate Password", corner_radius=40, width=200,
                                            fg_color="#dc6c60", text_color="white", hover_color="#E97777", command=generate_pass)
generate_password.place(x=100, y= 320)

add_button = customtkinter.CTkButton(master= window, text="Add", corner_radius=40, width=200,
                                     fg_color="#dc6c60", text_color="white", hover_color="#E97777", command=save_input)
add_button.place(x=100, y= 360)

copy_png = PhotoImage(file="copy-icon.png")
copy_button = Button(master= window, text="",  width=20, command=copyy, image=copy_png, compound= LEFT, borderwidth=0, bg="#f9f9fb", relief="flat", highlightthickness=0)
copy_button.place(x=270, y=286 )

search_png = PhotoImage(file="search.png")
search_button = Button(master= window, text="",  width=20, command=search, image=search_png, compound= LEFT, borderwidth=0, bg="#f9f9fb", relief="flat", highlightthickness=0)
search_button.place(x=270, y=205 )

#Codes for UI Configuration

def email_change(e_change):
    email.configure(border_color="#dc6c60")
def email_change1(e_change2):
    email.configure(border_color="#D1D1D1")
def website_change(web_change):
    website.configure(border_color="#dc6c60")
def website_change1(web_change2):
    website.configure(border_color="#D1D1D1")
def look_up(search1):
    search()

e_change = email.bind('<FocusIn>',email_change)
e_change2 = email.bind('<FocusOut>',email_change1)
web_change = website.bind('<FocusIn>',website_change)
web_change2 = website.bind('<FocusOut>',website_change1)
search1 = website.bind("<Return>", look_up)


window.mainloop()

