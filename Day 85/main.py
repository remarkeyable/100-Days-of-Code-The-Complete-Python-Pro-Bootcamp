import customtkinter
import csv
import random
from CTkMessagebox import CTkMessagebox


window = customtkinter.CTk()
window.minsize(width=300, height=500)
window.maxsize(width=300, height=500)
window.title("Typing Speed Test")

chosen_word = ""
word_counts = 0
list_of_scores = [{"Username": '', "Score": ''}, {"Username": '', "Score": ''}, {"Username": '', "Score": ''}]
asciiii = f''' 𝓡𝓮𝓬𝓮𝓷𝓽 𝓢𝓬𝓸𝓻𝓮𝓼 

{list_of_scores[-1]['Username']}  {list_of_scores[-1]['Score']} 
{list_of_scores[-2]['Username']}  {list_of_scores[-2]['Score']} 
{list_of_scores[-3]['Username']}  {list_of_scores[-3]['Score']} 
'''

with open('funny_usernames.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    user_names = list(reader)


def start(event):
    global chosen_word, entry, word_counts, timer, score, words

    if chosen_word == entry.get().lower() + event.char.lower():
        entry.delete(0, 'end')
        window.after(100, lambda: entry.delete(0, 'end'))
        word_counts += 1
        generate_word()
        words.configure(text=chosen_word)
    if len(chosen_word) < len(entry.get() + event.char):
        words.configure(text_color="#CA3E47")
    if len(chosen_word) > len(entry.get() + event.char):
        words.configure(text_color="#313131")


def generate_word():
    global chosen_word
    with open('words.csv') as text:
        words = list(text)
        chosen_word = random.choice(words).strip().lower()


def restart():
    global entry, word_counts, list_of_scores, word_counts, user_names, eme_scores, words, start_t
    start_t.configure(state='disabled')
    entry.configure(state="normal", border_color="#525252")
    word_counts = 0
    entry.delete(0, 'end')
    window.after(60000, lambda: entry.configure(state='disabled', border_color="#CA3E47"))
    window.after(60000, lambda: start_t.configure(state='normal'))
    window.after(60000, lambda: words.configure(text_color="#313131"))
    window.after(60001, lambda: list_of_scores.append(update_list()))
    window.after(60002, lambda: eme_scores.configure(text=f''' 𝓡𝓮𝓬𝓮𝓷𝓽 𝓢𝓬𝓸𝓻𝓮𝓼
 
{list_of_scores[-1]['Username'].strip("[]").replace("'", "")}  {list_of_scores[-1]['Score']} 
{list_of_scores[-2]['Username'].strip("[]").replace("'", "")}  {list_of_scores[-2]['Score']} 
{list_of_scores[-3]['Username'].strip("[]").replace("'", "")}  {list_of_scores[-3]['Score']} 
'''))


def update_list():
    current_user = {"Username": f'{random.choice(user_names)}', "Score": f"{round(word_counts * 1.5)} WMP"}
    return current_user


def score_res():
    CTkMessagebox(title="Info", message=asciiii, icon="")


generate_word()
words = customtkinter.CTkLabel(window, text=chosen_word, font=("Courier New", 35), text_color="#313131")
words.place(relx=0.5, rely=0.4, anchor="center")

entry = customtkinter.CTkEntry(window, width=200, height=40, font=('Courier New', 25), text_color="#525252",
                               state='disabled', border_color="#CA3E47")
entry.place(relx=0.5, rely=0.5, anchor="center")

start_t = customtkinter.CTkButton(window, text="Start", command=restart, width=200, height=40, fg_color="#525252",
                                  hover_color="#313131")
start_t.place(relx=0.5, rely=0.6, anchor="center")

eme_scores = customtkinter.CTkLabel(window, text=asciiii, font=("Courier New", 15), text_color="#313131")
eme_scores.place(relx=0.5, rely=0.2, anchor="center")

entry.focus()
entry.bind("<Key>", start)

window.mainloop()
