from tkinter import*
import requests
import random
from tkinter.messagebox import showinfo
import html
import customtkinter

class Ui:
    def __init__(self):
        self.score = 0
        self.quiz_count = 10
        self.start()
        self.window = Tk()
        self.window.minsize(400,650)
        self.window.configure(background="#86C8BC")
        self.window.title("Quiz App by Ryn")

        #Canvas
        self.canvas = Canvas(width=310, height=310, bg="#CEEDC7", borderwidth=2,
                             highlightthickness=0)
        self.label = self.canvas.create_text(150, 150, width=260,text="", font=("Arial Narrow", 15, "bold"), fill="#099A97")
        self.canvas.place(x= 43, y=70)

        #Buttons
        self.false = PhotoImage(file="./images/false.png")
        self.true = PhotoImage(file="./images/true.png")
        self.false_button = Button(width=100,height= 97, image=self.false, command= self.ans_false, highlightthickness=0 , borderwidth=0)
        self.true_button = Button(width= 100, height= 97, image=self.true, command= self.ans_true, highlightthickness=0 , borderwidth=0)
        self.false_button.place(x=80, y= 400)
        self.true_button.place(x=220, y=400)
        self.restart = customtkinter.CTkButton(master=self.window, text="Restart Game", width=200,
                                                height=30, fg_color="#6CC4A1", border_color="white",
                                                border_width=1, hover_color="#A9EEC2",
                                               text_color="white", command=self.restart)
        self.restart.place(x=97, y=590)

        # Text Score
        self.text_score = Label(text=f"Score:  {self.score} / {self.quiz_count}", font=("Arial", 12, "bold"), bg="#86c8bc", fg="#099A97")
        self.text_score.place(x= 45, y= 38)


        #Combo Box for Modes & quiz count
        self.combobox_var = customtkinter.StringVar(value="Difficulty")
        self.combobox = customtkinter.CTkComboBox(master=self.window,
                                                  values=["Easy", "Medium", "Hard"],
                                                  variable=self.combobox_var, button_color="#6CC4A1",
                                                  border_color="white", button_hover_color="#CFF6CF"
                                                  , width=200, height=30, justify="center", border_width=1,
                                                  dropdown_fg_color="#6CC4A1", dropdown_hover_color="#CFF6CF",
                                                  fg_color="#6CC4A1", text_color="white", command=self.difficulty, state="readonly")
        self.combobox.place(x=97, y=510)
        self.combobox_var2 = customtkinter.StringVar(value="Number of Questions")
        self.combobox2 = customtkinter.CTkComboBox(master=self.window,
                                                  values=["10", "20", "30", "40", "50"],
                                                  variable=self.combobox_var2, button_color="#6CC4A1",
                                                  border_color="white", button_hover_color="#CFF6CF"
                                                  , width=200, height=30, justify="center", border_width=1,
                                                  dropdown_fg_color="#6CC4A1", dropdown_hover_color="#CFF6CF",
                                                  fg_color="#6CC4A1", text_color="white", command=self.amount, state="readonly")
        self.combobox2.place(x=97, y=550)

        self.generate_ques()
        self.window.mainloop()

    #Will generate questions
    def generate_ques(self):
        try:
            self.text_score.configure(text=f"Score:  {self.score} / {self.quiz_count} ")
            self.current = random.choice(self.all_question)
            self.canvas.itemconfig(self.label, text=html.unescape(self.current[0]))
            self.all_question.remove(self.current)

        #If number of quiz already completed, the quiz generator will stop & true & false button will be disabled.
        except:
            showinfo(title="Warning", message= f"Quiz already completed. \n Your final score: {self.score}")
            self.false_button.configure(state="disabled")
            self.true_button.configure(state="disabled")

    #Will check the answer & add score if correct
    def scoring(self):
        if self.answer == self.current[1]:
            self.score += 1

    #Connected to True button
    def ans_true(self):
        self.answer = "True"
        self.scoring()
        self.text_score.configure(text=f"Score:  {self.score} / {self.quiz_count} ")
        self.generate_ques()

    # Connected to False button
    def ans_false(self):
        self.answer = "False"
        self.scoring()
        self.text_score.configure(text=f"Score:  {self.score} / {self.quiz_count}")
        self.generate_ques()

    # Connected to combobox, will change the amount of quiz of the game by changing the
    # requests parameter base on the combox value
    def amount(self,choice):
        self.quiz_count = choice
        self.parameters["amount"] = choice
        self.start()
        self.generate_ques()

    # Connected to combobox2, will change the difficulty mode of the game by changing the
    # requests parameter base on the combox value
    def difficulty(self, choice):
        self.parameters["difficulty"] = choice
        self.start()
        self.generate_ques()

    #Connected to restart button, everything will be refresh when this function execute
    def restart(self):
        self.score = 0
        self.text_score.configure(text=f"Score:  {self.score} / 10")
        self.false_button.configure(state="normal")
        self.true_button.configure(state="normal")
        self.combobox_var.set("Difficulty")
        self.combobox_var2.set("Number of Questions")
        self.start()
        self.generate_ques()
        showinfo(title="Info", message="Game restarted")

    #This is like the database of the game. will get the data from open trivia API and will turn it to a list.
    def start(self):
        self.parameters = {
            "amount": 10,
            "type": "boolean",
            "difficulty": "easy",

        }
        self.response = requests.get("https://opentdb.com/api.php", params=self.parameters)
        self.quiz = self.response.json()
        self.question = self.quiz['results']
        self.all_question = []
        self.current = ""
        self.answer = ""
        for i in self.question:
            self.ques = i['question']
            self.correct = i['correct_answer']
            self.all_question.append([self.ques, self.correct])










