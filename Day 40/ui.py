import re
import tkinter
from tkinter import *
import customtkinter
from tkinter import END
from tkcalendar import DateEntry
from data import Data
from sendmail import Sendmail
from tkinter import messagebox
data = Data()

class Ui:
    def __init__(self,combo):
        self.list = combo
        self.window = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
        self.window.minsize(450, 400)
        self.window.title("Flight Club")
        self.send_mail = ""
        self.cur = ""
        self.to = ""

        #Location Entry & List Box
        self.var = StringVar()
        self.var2 = StringVar()
        self.entry = customtkinter.CTkEntry(master=self.window, textvariable= self.var,
                                            width=170)
        self.entry.place(x=50, y=160)
        # self.wrapper = Frame(self.window, bd=2, relief="sunken")
        self.text_box = Listbox(master=self.window, width=27, height=2,
                                highlightcolor="#242424", bg="#242424", relief="flat", foreground="white",highlightbackground="#242424")
        self.text_box.place(x= 50, y= 190)
        self.entry2 = customtkinter.CTkEntry(master=self.window, textvariable=self.var2,
                                             width=170, placeholder_text="Select Destination")
        self.entry2.place(x=230, y= 160)
        self.text_box2 = Listbox(master=self.window, width=27, height=2,
                                relief="flat", highlightcolor="#242424", bg="#242424", bd=0, foreground="white",highlightbackground="#242424")
        self.text_box2.place(x=230, y=190)


        #Will trace the Entry(Location) and pass the value of selected text on List
        self.var.trace('w', self.read_data)
        self.entry.bind('<Down>', self.down)
        self.text_box.bind('<Right>', self.update)
        self.text_box.bind('<Return>', self.update)
        self.var2.trace('w', self.read_data2)
        self.entry2.bind('<Down>', self.down2)
        self.text_box2.bind('<Right>', self.update2)
        self.text_box2.bind('<Return>', self.update2)


        #Date picker
        self.date_var_to = StringVar()
        self.date_to = DateEntry(selectmode="day", textvariable=self.date_var_to, width=24)
        self.date_to.place( x=230, y=100)
        self.date_var_fr = StringVar()
        self.date_fr = DateEntry(selectmode="day", textvariable=self.date_var_fr, width=24)
        self.date_fr.place(x=50, y=100)


        #Text Labels
        self.title_label = Label(text="Flight Club", fg="white", bg="#242424",font=("Arial", 25))
        self.title_label.place(x=135, y=20)
        self.fr_label = Label(text="Select Origin", fg="white", bg="#242424")
        self.fr_label.place(x=50, y=137)
        self.to_label = Label(text="Select Destination", fg="white", bg="#242424")
        self.to_label.place(x=230, y=137)
        self.fr_d_label = Label(text="Date range from", fg="white", bg="#242424")
        self.fr_d_label.place(x=50, y=75)
        self.to_d_label = Label(text="Date range to", fg="white", bg="#242424")
        self.to_d_label.place(x=230 ,y=75)

        #Sumbit button will get the value on entries and execute the function on search Data class
        self.submit_button = customtkinter.CTkButton(master= self.window, text="Submit", command=self.get_to)
        self.submit_button.place(x= 155, y= 280)


        self.email = customtkinter.CTkEntry(master= self.window, width=240,placeholder_text="Your Email")
        self.email.place(x=110, y= 230)
        # self.budget = customtkinter.CTkEntry(master=self.window, width=240, placeholder_text="Your budget")
        # self.budget.place(x=110, y=270)

        #Check buttons
        # self.check_var = StringVar(value="yes")
        # self.check = customtkinter.CTkCheckBox(master= self.window, text= "Email the current lowest price")
        # self.check.place(x=110, y= 310)
        # self.check_var2 = StringVar(value="yes")
        # self.check2 = customtkinter.CTkCheckBox(master=self.window, text="Email base on my budget")
        # self.check2.place(x=110, y=340)
        self.window.mainloop()

    def read_data(self,*args):
        self.search = self.entry.get()
        self.text_box.delete(0,END)
        for letters in self.list:
            if(re.match(self.search, letters, re.IGNORECASE)):
                self.text_box.insert(tkinter.END, letters)
        if self.search == "":
            self.text_box.delete(0, END)

    def update(self,my_widget):
        self.window = my_widget.widget
        self.index = int(self.window.curselection()[0])
        self.value = self.window.get(self.index)
        self.var.set(self.value)
        self.text_box.delete(0,END)


    def down(self,my_widget):
        self.text_box.focus()
        self.text_box.selection_set(0)


    def read_data2(self,*args):
        self.search = self.entry2.get()
        self.text_box2.delete(0,END)
        for letters in self.list:
            if(re.match(self.search, letters, re.IGNORECASE)):
                self.text_box2.insert(tkinter.END, letters)
        if self.search == "":
            self.text_box2.delete(0, END)


    def update2(self,my_widget):
        self.window = my_widget.widget
        self.index = int(self.window.curselection()[0])
        self.value = self.window.get(self.index)
        self.var2.set(self.value)
        self.text_box2.delete(0,END)


    def down2(self,my_widget):
        self.text_box2.focus()
        self.text_box2.selection_set(0)

    #will execute the important process like getting the variables from entry and triggering send mail function
    def get_to(self):
        self.cur = self.entry.get()
        self.to = self.entry2.get()
        self.dateconvert = self.date_fr.get_date()
        self.date1 = self.dateconvert.strftime("%d/%m/%Y")
        self.date2convert = self.date_to.get_date()
        self.date2 = self.date2convert.strftime("%d/%m/%Y")
        self.cur1 = data.iata(self.cur)
        self.to2 = data.iata(self.to)
        data.search(self.cur1, self.to2, self.date1, self.date2)
        self.send_mail = self.email.get()
        Sendmail(mail=self.send_mail, price=data.price, link=data.link, current_loc=self.cur, to_loc=self.to)
        self.entry.delete(0,END)
        self.entry2.delete(0,END)
        self.date_to.delete(0,END)
        self.date_fr.delete(0, END)
        self.email.delete(0,END)
        messagebox.showinfo(title="Info", message="Email Sent ~")




