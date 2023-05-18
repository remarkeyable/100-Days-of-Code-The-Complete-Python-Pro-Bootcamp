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
window.minsize(width=450, height=750)
window.maxsize(width=450, height=750)
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


def submit():
    global loc
    global mark_entry
    global my_label

    file_name = os.path.basename(loc)
    img1 = Image.open(fr"{loc}")
    print(img1.size)
    img2 = ImageTk.PhotoImage(img1)
    my_label.config(image=img2)
    my_label.pack(pady=20)
    my_label.image = img2

    draw = ImageDraw.Draw(img1)
    text = mark_entry.get()
    font = ImageFont.truetype("images/Bertha.ttf", 30)
    w, h = img1.size
    width = int(w - 500)
    height = int(h - 300)
    print(width)
    draw.text((597, height), text=text, font=font)
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


img = ImageTk.PhotoImage(file="images/1.jpg")
my_label = Label(window, image=img, width=400, height=400, borderwidth=1, bg="#2e2a2a")
my_label.pack(pady=20)

tabview = customtkinter.CTkTabview(master=window, fg_color="#2e2a2a", width=400, height=400)
tabview.pack(padx=20, pady=20)

tabview.add("Text Watermark")  # add tab at the end
tabview.add("Logo Watermark")  # add tab at the end
tabview.set("Text Watermark")  # set currently visible tab

# Text Tab
button = customtkinter.CTkButton(master=tabview.tab("Text Watermark"), text="Open image", command=image_loc, width=200)
button.place(y=15, x=95)

mark_entry = customtkinter.CTkEntry(master=tabview.tab("Text Watermark"), placeholder_text="Text watermark", width=200)
mark_entry.place(y=55, x=95)

set_value = StringVar(value='Top Right')
position = customtkinter.CTkComboBox(master=tabview.tab("Text Watermark"), values=["Top Right", "Top Left", "Down Right", "Down Left", "Middle", "Middle Top", "Middle Down"],
                                     width=200, state="readonly", variable=set_value)
position.place(y=95, x=95)

font_size = customtkinter.CTkComboBox(master=tabview.tab("Text Watermark"), values=["1", "2"], width=60)
font_size.place(y=135, x=235)

f_set_value = StringVar(value='Fonts')
fonts = customtkinter.CTkComboBox(master=tabview.tab("Text Watermark"), values=["adsadasdasdasdasdasd", "b", "c"],
                                  width=130)
fonts.place(y=135, x=95)


def test():
    print(position.get())


submit_button = customtkinter.CTkButton(master=tabview.tab("Text Watermark"), text="Submit", command=submit, width=200)
submit_button.place(y=175, x=95)

# Logo Tab
logo_button = customtkinter.CTkButton(master=tabview.tab("Logo Watermark"), text="Open image", command=image_loc,
                                      width=200)
logo_button.place(y=15, x=95)

logo_size = customtkinter.CTkComboBox(master=tabview.tab("Logo Watermark"), values=["1", "2"], width=60)
logo_size.place(y=55, x=235)

logo_position = customtkinter.CTkComboBox(master=tabview.tab("Logo Watermark"),
                                          values=["adsadasdasdasdasdasd", "b", "c"], width=130)
logo_position.place(y=55, x=95)

window.mainloop()
