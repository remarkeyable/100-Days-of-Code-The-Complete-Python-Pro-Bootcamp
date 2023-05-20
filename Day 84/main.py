import os.path
import os
import shutil
import tkinter
from tkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import ImageTk, ImageFont, ImageDraw, Image
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import time

window = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
window.minsize(width=450, height=780)
window.maxsize(width=450, height=780)
window.title("Katara")

height = 0
width = 0
loc = ""

def image_loc():
    global loc, mark_entry, height , width

    image = filedialog.askopenfile(mode='r',
                                   filetypes=[('Jpg Files', '*.jpg'), ('PNG Files', '*.png'), ('TIFF Files', '*.tiff'),
                                              ('HEIC Files', '*.heic')])
    if image:
        image_path = os.path.abspath(image.name)
        loc = image_path
        img1 = Image.open(fr"{image_path}")
        w, h = img1.size
        width = int(w)
        height = int(h)
        img1.thumbnail((400, 400))
        img2 = ImageTk.PhotoImage(img1)
        my_label.config(image=img2)
        my_label.pack(pady=20)
        my_label.image = img2



def edit(value):
    global loc, mark_entry, my_label, width, height, position_x, position_y, font_size, fonts

    file_name = os.path.basename(loc)
    img1 = Image.open(fr"{loc}")
    img1.thumbnail((400, 400))
    img2 = ImageTk.PhotoImage(img1)

    my_label.config(image=img2)
    my_label.pack(pady=20)
    my_label.image = img2

    draw = ImageDraw.Draw(img1)
    text = mark_entry.get()

    w, h = img1.size
    position_y.configure(from_=0, to=int(h))
    position_x.configure(from_=0, to=int(w))

    try:
        font = ImageFont.truetype(f"fonts/{fonts.get()}.ttf", int(font_size.get()))
        draw.text((int(position_x.get()), int(position_y.get())), text=text, font=font)


    except:
        CTkMessagebox(title="Info", message="Font size invalid, please double check your input", width=150, icon_size=(30, 30), )
        font_size.set("150")




    img1.save(f"edited/edited_{file_name}")

    edited = Image.open(f"edited/edited_{file_name}")
    edited.thumbnail((400, 400))
    edited1 = ImageTk.PhotoImage(edited)
    my_label.config(image=edited1)
    my_label.pack(pady=20)
    my_label.image = edited1


def save_pic():
    mark_entry.delete(0, END)
    file_name = os.path.basename(loc)
    shutil.move(f"edited/edited_{file_name}",f"save_pics/edited_{file_name}")
    CTkMessagebox(title="Info", message="Image Saved", width=150,
                  icon_size=(30, 30), )
    font_size.set("150")




img = ImageTk.PhotoImage(file="images/start.jpg")
my_label = Label(window, image=img, width=400, height=400, borderwidth=1, bg="#2e2a2a")
my_label.pack(pady=20)

tabview = customtkinter.CTkTabview(master=window, fg_color="#2e2a2a", width=400, height=450)
tabview.pack(padx=20, pady=20)

tabview.add("Text Watermark")  # add tab at the end
tabview.add("Logo Watermark")  # add tab at the end
tabview.set("Text Watermark")  # set currently visible tab

# Text Tab
button = customtkinter.CTkButton(master=tabview.tab("Text Watermark"), text="Open image", command=image_loc, width=215)
button.place(y=15, x=86)

mark_entry = customtkinter.CTkEntry(master=tabview.tab("Text Watermark"), placeholder_text="Text watermark", width=215)
mark_entry.place(y=55, x=86)


position_y = customtkinter.CTkSlider(master=tabview.tab("Text Watermark"), from_=0 , to=700, command=edit, width=215, )
position_y.set(0)
position_y.place(y=100, x=88)

position_x = customtkinter.CTkSlider(master=tabview.tab("Text Watermark"), from_=0 , to=700, command=edit, width=210)
position_x.set(0)
position_x.place(y=125, x=88)

list = range(1,21)
sizes = [str(i) for i in list]
list_fonts = ["ArialTh","Autography","Bertha","Cakecafe","Calibri","Delight Sunset","Fragmentcore","Punk-Typewriter","Slimshoot"]

font_size = customtkinter.CTkComboBox(master=tabview.tab("Text Watermark"), values=sizes, width=65, command=edit)
font_size.set("150")
font_size.place(y=160, x=230)


fonts = customtkinter.CTkComboBox(master=tabview.tab("Text Watermark"), values=list_fonts,
                                  width=135, command=edit)
fonts.set("Calibri")
fonts.place(y=160, x=86)



submit_button = customtkinter.CTkButton(master=tabview.tab("Text Watermark"), text="Submit", command=save_pic, width=215)
submit_button.place(y=205, x=86)














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
