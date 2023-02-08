PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
res_timer = None

from tkinter import *
import customtkinter
import math

window = Tk()
window.title("Pomorado")
window.minsize(width= 400, height=400)
window.config(padx=50,pady=40, bg=YELLOW)

def off():
    start_button.configure(state= DISABLED, fg_color="#FF8C8C" )
def on():
    start_button.configure(state= NORMAL, fg_color="#f26849")
def reset():
    on()
    window.after_cancel(res_timer)
    canvas.itemconfig(timer, text="00:00")
    up_label.config(text="Timer")
    up_label.place(x=100, y=0)
    global reps
    reps = 0
def start():
   global reps
   reps +=1
   work = WORK_MIN * 60
   short = SHORT_BREAK_MIN * 60
   long = LONG_BREAK_MIN * 60
   if reps % 8 == 0:
       count_down(long)
       print(reps)
       up_label.config(text= "Long break")
       up_label.place(x= 80, y= 0)

   elif reps % 2 == 0:
       up_label.config(text="Short break")
       up_label.place(x=55, y=0)
       print(reps)
       count_down(short)
       if reps == 6:
           on()
   else:
       up_label.config(text="Work break")
       up_label.place(x=60, y=0)
       count_down(work)
       if reps != 6:
           off()

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global res_timer
        res_timer = window.after(1000, count_down, count -1)
    else:
        start()

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato)
timer = canvas.create_text(102, 130, text="00:00", fill="#FFFBEB", font=(FONT_NAME, 25, "bold"))
canvas.place(x=55, y= 50)

start_button = customtkinter.CTkButton(master= window,text="Start", text_color= "white", command=start, corner_radius=50, fg_color="#f26849", hover_color="#FF8C8C", width=80 )
start_button.place(x= -2, y= 240)

reset_button = customtkinter.CTkButton(master= window,text="Reset",text_color= "white", command=reset, corner_radius=50, fg_color="#f26849", hover_color="#FF8C8C", width=80 )
reset_button.place(x= 230, y= 240)

up_label = Label(text = "Timer", bg=YELLOW, fg="#379b46", font=(FONT_NAME, 23, "bold"))
up_label.place(x= 100, y= 0)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()





