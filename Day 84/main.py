import os.path
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, ImageFont, ImageDraw, Image
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile


window = customtkinter.CTk()
window.maxsize(width=600,height=600)
window.title("Katara")
def image_loc():
    image = filedialog.askopenfile(mode='r', filetypes=[('Jpg Files', '*.jpg'),('PNG Files','*.png'),('TIFF Files','*.tiff'),('HEIC Files','*.heic')])
    if image:
        global  my_label
        image_path = os.path.abspath(image.name)
        print(image_path)
        img1 = Image.open(fr"{image_path}")
        img1.thumbnail((500,500))
        img2 = ImageTk.PhotoImage(img1)
        my_label.config(image=img2)
        my_label.pack(pady=20)
        my_label.image = img2


button = customtkinter.CTkButton(window, text="test",  command=image_loc)
button.pack()
aspen = ImageTk.PhotoImage(file="images/aa.jpg")
my_label = Label(window, image=aspen)
my_label.pack(pady=20)


window.mainloop()
