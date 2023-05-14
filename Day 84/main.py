import os.path
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, ImageFont, ImageDraw, Image
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile


window = customtkinter.CTk()
window.minsize(width=800,height=800)
window.title("Katara")
import time
def image_loc():
    image = filedialog.askopenfile(mode='r', filetypes=[('Jpg Files', '*.jpg'),('PNG Files','*.png'),('TIFF Files','*.tiff'),('HEIC Files','*.heic')])
    if image:
        global  my_label
        image_path = os.path.abspath(image.name)
        print(image_path)


        test = Image.open(fr"{image_path}")

        if test.width > 540 and test.height > 540:
            resized_image = test.resize((540, 540), Image.Resampling.LANCZOS)
        elif test.width > 540:
            resized_image = test.resize((540, test.height), Image.Resampling.LANCZOS)
        elif test.height > 540:
            resized_image = test.resize((test.width, 540), Image.Resampling.LANCZOS)
        else:
            resized_image = test

        # resize = test.resize((200,200),  Image.Resampling.LANCZOS)
        aspen = ImageTk.PhotoImage(resized_image)
        my_label.config(image=aspen)
        my_label.pack(pady=20)
        my_label.image = aspen


# def view_pic():
#     aspen = ImageTk.PhotoImage(file=fr"{image_loc()}")
#     print("done")
#     my_label.config(window, image=aspen)
#     my_label.pack(pady=20)
#     print(image_loc())



button = customtkinter.CTkButton(window, text="test",  command=image_loc)
button.pack()
#
aspen = ImageTk.PhotoImage(file="images/aa.jpg")
my_label = Label(window, image=aspen)
my_label.pack(pady=20)


window.mainloop()
