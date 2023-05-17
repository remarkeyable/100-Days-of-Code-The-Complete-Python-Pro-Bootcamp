import os.path
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, ImageFont, ImageDraw, Image
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import time

window = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
window.minsize(width=600, height=700)
window.maxsize(width=600, height=700)
window.title("Katara")

loc = ""
f_size = 0

def image_loc():
    global loc
    global mark_entry
    image = filedialog.askopenfile(mode='r',
                                   filetypes=[('Jpg Files', '*.jpg'), ('PNG Files', '*.png'), ('TIFF Files', '*.tiff'),
                                              ('HEIC Files', '*.heic')])
    if image:
        image_path = os.path.abspath(image.name)
        loc = image_path
        img1 = Image.open(fr"{image_path}")
        img1.thumbnail((400, 400))
        img2 = ImageTk.PhotoImage(img1)
        my_label.config(image=img2)
        my_label.pack(pady=20)
        my_label.image = img2


def submit(value):
    global loc
    global mark_entry
    global my_label

    file_name = os.path.basename(loc)
    img1 = Image.open(fr"{loc}")
    img2 = ImageTk.PhotoImage(img1)
    my_label.config(image=img2)
    my_label.pack(pady=20)
    my_label.image = img2

    draw = ImageDraw.Draw(img1)
    text = mark_entry.get()
    font = ImageFont.truetype("images/Bertha.ttf", int(value))
    draw.text((10, 10), text=text, font=font)
    img1.save(f"edited/edited_{file_name}")

    edited = Image.open(f"edited/edited_{file_name}")
    edited.thumbnail((400, 400))
    edited1 = ImageTk.PhotoImage(edited)
    my_label.config(image=edited1)
    my_label.pack(pady=20)
    my_label.image = edited1

    # mark_entry.delete(0, END)


def slider_event(value):
    global f_size
    f_size = value



button = customtkinter.CTkButton(window, text="Open image", command=image_loc)
button.place(y=450, x=230)
aspen = ImageTk.PhotoImage(file="images/1.jpg")
my_label = Label(window, image=aspen, width=400, height=400, borderwidth=1, bg="#282424")
my_label.pack(pady=20)
mark_entry = customtkinter.CTkEntry(window, placeholder_text="Text watermark")
mark_entry.place(y=490, x=230)
font_size = customtkinter.CTkSlider(window, from_=0, to=400, width=140, command=submit)
font_size.place(y=530, x=228)

fonts = customtkinter.CTkComboBox(window, values=["a","b","c"])
fonts.place(y=560, x=230)
submit_button = customtkinter.CTkButton(window, text="Submit", command=submit)
submit_button.place(y=600, x=230)

window.mainloop()
