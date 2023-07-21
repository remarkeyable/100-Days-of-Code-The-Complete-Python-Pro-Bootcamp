import customtkinter
from tkinter import ttk, filedialog
from gtts import gTTS
import os, os.path
from PyPDF2 import PdfReader

window = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)

the_file_path = ""


def open_pdf():
    global the_file_path

    pdf = filedialog.askopenfile(mode='r', filetypes=[('Pdf Files', '*.pdf')])

    if pdf:
        file = pdf.name
        pdf_path = os.path.abspath(file)
        the_file_path = pdf_path
        pdf_text = ""
        read_pdf = PdfReader(the_file_path)
        number_of_pages = len(read_pdf.pages)
        for i in range(number_of_pages):
            page = read_pdf.pages[i]
            pdf_text += page.extract_text()

        tts = gTTS(pdf_text, lang='en', tld='com.au')

        tts.save('audio.mp3')


def play_audio():
    os.startfile('audio.mp3')


get_pdf = customtkinter.CTkButton(window, text="Open PDF", command=open_pdf, width=150, height=50)
get_pdf.place(x=175, y=200)

play_pdf = customtkinter.CTkButton(window, text="Play Audio", command=play_audio, width=150, height=50)
play_pdf.place(x=175, y=260)

window.mainloop()
