BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
import customtkinter

class Languages():
    def __init__(self, language):
        self.language = language
        self.window = Tk()
        self.window.title("Flashcard")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        #Open the csv file
        with open (f"./data/{self.language}_words.csv") as self.open:
            self.open = pandas.read_csv(f"./data/{self.language}_words.csv")
            self.open2 = pandas.read_csv(f"./data/{self.language}.csv")
            self.words_to_learn = self.open2.to_dict(orient="records")
            self.original = self.open.to_dict(orient="records")
            self.current = {}

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

        # Language Label.
        self.text = Label(text="", font=("Arial", 40, "normal"), bg="white")
        self.text.grid(row=0, column=0, columnspan=2)
        self.timer = self.window.after(3000, func=self.flip)
        self.generate_words()

        #ComboBox holds the languages
        self.combobox_var = customtkinter.StringVar(value="Languages")
        self.combobox = customtkinter.CTkComboBox(master=self.window,
                                                  values=["Japanese", "French", "Korean"],
                                                  command=self.changes,
                                                  variable=self.combobox_var, button_color="#91c2af",
                                                  border_color="#91c2af", button_hover_color= "#CFF6CF"
                                                  ,width= 200, height=30, justify="center", border_width=3)
        self.combobox.grid(row=1, column=0, columnspan=2)
        self.window.mainloop()

    def generate_words(self):

        self.window.after_cancel(self.timer)
        self.current = random.choice(self.words_to_learn)
        self.canvas.itemconfig(self.background, image=self.card_front)
        self.canvas.itemconfig(self.card_title, text=f"{self.language}", fill="black")
        self.text.configure(text=self.current[f'{self.language}'], bg="white", fg="black")
        self.timer = self.window.after(3000, func=self.flip)

    def remove_word(self):
       self.words_to_learn.remove(self.current)
       self.df = pandas.DataFrame(self.words_to_learn)
       # self.df.to_csv(f"data/{language}_words_to_learn.csv", index=False)
       self.generate_words()

    # will flip the card & reveal the english translation
    def flip(self):
       self.canvas.itemconfig(self.card_title, text="English", fill="white")
       self.canvas.itemconfig(self.background, image=self.card_back)
       self.text.configure(text=self.current['English'], bg="#91c2af", fg="white")

    def skip(self):
        self.generate_words()

    #Connected to combo box, will change the language
    def changes(self,choice):
        self.language = choice
        with open (f"./data/{self.language}_words.csv") as self.open:
            self.open = pandas.read_csv(f"./data/{self.language}_words.csv")
            self.open2 = pandas.read_csv(f"./data/{self.language}.csv")
            self.words_to_learn = self.open2.to_dict(orient="records")
            self.original = self.open.to_dict(orient="records")
            self.current = {}
