
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
import customtkinter
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

class Languages():
    def __init__(self, language):
        self.language = language
        self.user_name = ""

        self.window = Tk()
        self.window.title("Flashcard")
        self.window.config(padx=50, pady=80, bg=BACKGROUND_COLOR)

        #Open the csv file
        with open (f"./data/Default_{self.language}.csv") as self.open:
            self.open = pandas.read_csv(f"./data/Default_{self.language}.csv", encoding='latin-1')
            self.header = self.open.columns
            self.current_lang = self.header[0]
            self.current_lang2 = self.header[1]
            self.words_to_learn = self.open.to_dict(orient="records")
            self.current = {}
        self.label = self.current_lang
        #____________UI__SETUP_________#
        # images
        self.card_back = PhotoImage(file="./images/card_back.png")
        self.card_front = PhotoImage(file="./images/card_front.png")
        self.check_image = PhotoImage(file="./images/right.png")
        self.eks_image = PhotoImage(file="./images/wrong.png")
        self.timer = self.window.after(3000)

        # canvas
        self.canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.background = self.canvas.create_image(0, 10, image=self.card_front, anchor=NW)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 45, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2)

        # buttons
        self.check_button = Button(width=100, height=100, image=self.check_image, highlightthickness=0, borderwidth=0, command=self.remove_word)
        self.eks_button = Button(width=100, height=100, image=self.eks_image, highlightthickness=0, borderwidth=0, command= self.skip)
        self.check_button.grid(row=1, column=1)
        self.eks_button.grid(row=1, column=0)
        self.download = customtkinter.CTkButton(master=self.window ,text="Download to review", width= 200,
                                                height=30, fg_color="#6CC4A1", border_color="white",
                                                border_width=1, hover_color="#A9EEC2", text_color="white", command=self.dialog_box)
        self.download.place(x= 300, y=  675)
        self.cont_progress = customtkinter.CTkButton(master=self.window, text="Login", width=200,
                                                height=30, fg_color="#6CC4A1", border_color="white",
                                                border_width=1, hover_color="#A9EEC2", text_color="white",
                                                command=self.cont)
        self.cont_progress.place(x=300, y=635)
        # Language Label.
        self.text = Label(text="", font=("Arial", 40, "normal"), bg="white")
        self.text.grid(row=0, column=0, columnspan=2)
        self.timer = self.window.after(3000, func=self.flip)
        self.generate_words()

        #ComboBox holds the languages
        self.combobox_var = customtkinter.StringVar(value="Languages")
        self.combobox = customtkinter.CTkComboBox(master=self.window,
                                                  values=["Japanese", "French", "Korean", "Filipino"],
                                                  command=self.changes,
                                                  variable=self.combobox_var, button_color="#6CC4A1",
                                                  border_color="white", button_hover_color= "#CFF6CF"
                                                  ,width= 200, height=30, justify="center", border_width=1,
                                                  dropdown_fg_color="#6CC4A1", dropdown_hover_color="#CFF6CF", fg_color="#6CC4A1", text_color="white")
        self.combobox.place( x= 300, y= 595 )
        self.welcome = customtkinter.CTkButton(master=self.window, text="Hello, Guest ~", width=200,
                                                height=30, fg_color="#78ca74", border_color="white",
                                                border_width=1, hover_color="#A0D995", text_color="white")
        self.welcome.place(x= 300, y= 555)

        self.window.mainloop()

    def generate_words(self):
        try:
            self.window.after_cancel(self.timer)
            self.current = random.choice(self.words_to_learn)
            self.canvas.itemconfig(self.background, image=self.card_front)
            self.canvas.itemconfig(self.card_title, text=f"{self.label}", fill="black")
            self.text.configure(text=self.current[f'{self.language}'], bg="white", fg="black")
            self.timer = self.window.after(3000, func=self.flip)
        except IndexError:
            pass

    #connected to x button, will remove words(known words) from words to learn dictionary
    def remove_word(self):
        try:
            self.words_to_learn.remove(self.current)
        except ValueError:
            showinfo("Warning","Out of words. Please choose different language")
        self.generate_words()


    # will flip the card & reveal the english translation
    def flip(self):
       self.canvas.itemconfig(self.card_title, text=f"{self.current_lang2}", fill="white")
       self.canvas.itemconfig(self.background, image=self.card_back)
       self.text.configure(text=self.current[f'{self.current_lang2}'], bg="#91c2af", fg="white")

    def skip(self):
        self.generate_words()

    #Connected to combo box, will change the language
    def changes(self,choice):
        self.language = choice
        with open(f"./data/Default_{self.language}.csv") as self.open:
            self.open = pandas.read_csv(f"./data/Default_{self.language}.csv",encoding='latin-1')
            self.words_to_learn = self.open.to_dict(orient="records")
            self.header = self.open.columns
            self.current_lang = self.header[0]
            self.label = self.current_lang
        self.generate_words()


    #connected to download button, will ask the user name and will use as a file name
    def dialog_box(self):
        self.name = askstring('Name', 'What is your name?').title()
        on = True
        while on:
            if self.name == "" :
                showinfo("Warning", "Name can't be blank, please input your name")
                self.name = askstring('Name', 'What is your name?')
            else:
                on = False
                self.df = pandas.DataFrame(self.words_to_learn)
                self.df.to_csv(f"./data/{self.name}_{self.language}.csv", index= False)
                showinfo('Info', f"Hi! {self.name}, your file has been successfully saved." )


    #Connected to login button, will continue the progress of user
    def cont(self):
        self.name = askstring('Name', 'What is your name?')
        try:
            with open(f"./data/{self.name}_{self.language}.csv") as self.open:
                self.open = pandas.read_csv(f"./data/{self.name}_{self.language}.csv", encoding='latin-1')
                self.words_to_learn = self.open.to_dict(orient="records")
                self.change_label()
                self.current = {}
                self.generate_words()
                self.welcome.configure(text=f"Hello, {self.name} ~")
        except FileNotFoundError:
            showinfo("Info", "No record found.")
            self.language = "Japanese"
            with open(f"./data/Default_Japanese.csv") as self.open:
                self.open = pandas.read_csv(f"./data/Default_Japanese.csv",encoding='latin-1')
                self.words_to_learn = self.open.to_dict(orient="records")
                self.change_label()
                self.current = {}
                if self.name == "":
                    self.welcome.configure(text=f"Hello, Guest ~")
                else:
                    pass
            self.generate_words()


    def change_label(self):
        self.header = self.open.columns
        self.current_lang = self.header[0]
        self.label = self.current_lang
        self.language = self.label