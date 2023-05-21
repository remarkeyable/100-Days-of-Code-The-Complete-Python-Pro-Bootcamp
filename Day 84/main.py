import os.path
import os
import shutil
from tkinter import *
from tkinter import colorchooser
import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import ImageTk, ImageFont, ImageDraw, Image
from tkinter import ttk, filedialog

window = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
window.minsize(width=450, height=810)
window.maxsize(width=450, height=810)
window.maxsize(width=450, height=810)
window.title("Katara")

height = 0
width = 0
loc = ""
logo_loc = ""
the_color = (255, 255, 255)


def image_loc():
    global loc, mark_entry, height, width
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
        # Preview image, img1.thumbnail to fit the image to Label without stretching
        img1.thumbnail((400, 400))
        img2 = ImageTk.PhotoImage(img1)
        my_label.config(image=img2)
        my_label.pack(pady=20)
        my_label.image = img2


def get_logo():
    global logo_loc
    image = filedialog.askopenfile(mode='r',
                                   filetypes=[('Jpg Files', '*.jpg'), ('PNG Files', '*.png'), ('TIFF Files', '*.tiff'),
                                              ('HEIC Files', '*.heic')])
    if image:
        image_path = os.path.abspath(image.name)
        logo_loc = image_path


def edit_text(value):
    global loc, mark_entry, my_label, width, height, position_x, position_y, font_size, fonts, the_color
    try:
        file_name = os.path.basename(loc)
        img1 = Image.open(fr"{loc}")
        draw = ImageDraw.Draw(img1)
        text = mark_entry.get()
        w, h = img1.size

        # Will configure the Ctk Slider to adjust the maximum number base on image size
        position_y.configure(from_=0, to=int(h))
        position_x.configure(from_=0, to=int(w))

        try:
            font = ImageFont.truetype(f"fonts/{fonts.get()}.ttf", int(font_size.get()))
            draw.text((int(position_x.get()), int(position_y.get())), text=text, font=font,
                      fill=tuple(map(int, the_color)))

        except:
            CTkMessagebox(title="Info", message="Font size invalid, please double check your input", width=150,
                          icon_size=(30, 30), icon="cancel")
            font_size.set("150")

        # Will save the edited image
        img1.save(f"edited/hd_edited_{file_name}")
        edited = Image.open(f"edited/hd_edited_{file_name}")
        edited.thumbnail((400, 400))
        # & configure the label
        edited1 = ImageTk.PhotoImage(edited)
        my_label.config(image=edited1)
        my_label.pack(pady=20)
        my_label.image = edited1
    except:
        CTkMessagebox(title="Info", message="No image selected", width=150, icon_size=(30, 30), icon="warning")
        font_size.set("150")


def edit_logo(value):
    global loc, logo_loc, lg_position_x, lg_position_y, lg_size
    file_name = os.path.basename(loc)
    img1 = Image.open(fr"{loc}")
    logo = Image.open(fr"{logo_loc}")

    lw, lh = logo.size
    lg_size.configure(from_=5, to=int(lw))

    logo.thumbnail((int(lg_size.get()), int(lg_size.get())))
    w, h = img1.size

    lg_position_y.configure(from_=0, to=int(h))
    lg_position_x.configure(from_=0, to=int(w))

    try:
        # addding the logo to the image
        img1.paste(logo, (int(lg_position_x.get()), int(lg_position_y.get())), logo)
        img1.save(f"edited/hd_edited_{file_name}")
    except ValueError:
        # if the logo is not png, this will execute, we remove the third parameter which indicate a mask
        img1.paste(logo, (int(lg_position_x.get()), int(lg_position_y.get())))
        img1.save(f"edited/hd_edited_{file_name}")

    edited = Image.open(f"edited/hd_edited_{file_name}")
    edited.thumbnail((400, 400))
    # & configure the label
    edited1 = ImageTk.PhotoImage(edited)
    my_label.config(image=edited1)
    my_label.pack(pady=20)
    my_label.image = edited1


def color_pic():
    global the_color
    pick_color = colorchooser.askcolor()
    the_color = pick_color[0]


def save_pic():
    # Will delete the input on entry box
    try:
        mark_entry.delete(0, END)
        file_name = os.path.basename(loc)
        # Final image will be move to another folder
        shutil.move(f"edited/hd_edited_{file_name}", f"save_pics/hd_edited_{file_name}")
        CTkMessagebox(title="Info", message="Image Saved", width=150, icon_size=(30, 30), icon="check")
        font_size.set("150")
    except FileNotFoundError:
        CTkMessagebox(title="Info", message="Something went wrong. Image empty as you.", width=150, icon_size=(30, 30), icon="cancel")
        font_size.set("150")


# Label, which handle the image
img = ImageTk.PhotoImage(file="images/start.jpg")
my_label = Label(window, image=img, width=400, height=400, borderwidth=1, bg="#2e2a2a")
my_label.pack(pady=20)

# Tab View
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

position_y = customtkinter.CTkSlider(master=tabview.tab("Text Watermark"), from_=0, to=700, command=edit_text,
                                     width=215, )
position_y.set(0)
position_y.place(y=100, x=88)

position_x = customtkinter.CTkSlider(master=tabview.tab("Text Watermark"), from_=0, to=700, command=edit_text,
                                     width=210)
position_x.set(0)
position_x.place(y=125, x=88)

list = range(1, 21)
sizes = [str(i) for i in list]
list_fonts = ["ArialTh", "Autography", "Bertha", "Cakecafe", "Calibri", "Delight Sunset", "Fragmentcore",
              "Punk-Typewriter", "Slimshoot"]

font_size = customtkinter.CTkComboBox(master=tabview.tab("Text Watermark"), values=sizes, width=65, command=edit_text)
font_size.set("150")
font_size.place(y=160, x=230)
fonts = customtkinter.CTkComboBox(master=tabview.tab("Text Watermark"), values=list_fonts, width=135, command=edit_text)
fonts.set("Calibri")
fonts.place(y=160, x=86)

color = customtkinter.CTkButton(master=tabview.tab("Text Watermark"), text="Pick Color", command=color_pic, width=215)
color.place(y=205, x=86)

submit_button = customtkinter.CTkButton(master=tabview.tab("Text Watermark"), text="Save", command=save_pic, width=215)
submit_button.place(y=245, x=86)

# Logo Tab
logo_button = customtkinter.CTkButton(master=tabview.tab("Logo Watermark"), text="Open image", command=image_loc,
                                      width=215)
logo_button.place(y=15, x=86)

add_logo_button = customtkinter.CTkButton(master=tabview.tab("Logo Watermark"), text="Add logo", command=get_logo,
                                          width=215)
add_logo_button.place(y=55, x=86)

lg_position_y = customtkinter.CTkSlider(master=tabview.tab("Logo Watermark"), from_=0, to=700, command=edit_logo,
                                        width=215, )
lg_position_y.set(0)
lg_position_y.place(y=95, x=88)

lg_position_x = customtkinter.CTkSlider(master=tabview.tab("Logo Watermark"), from_=0, to=700, command=edit_logo,
                                        width=210)
lg_position_x.set(0)
lg_position_x.place(y=125, x=88)

lg_size = customtkinter.CTkSlider(master=tabview.tab("Logo Watermark"), from_=5, to=700, command=edit_logo, width=210)
lg_size.set(100)
lg_size.place(y=155, x=88)

lg_save = customtkinter.CTkButton(master=tabview.tab("Logo Watermark"), text="Save", command=save_pic, width=215)
lg_save.place(y=185, x=86)

window.mainloop()
