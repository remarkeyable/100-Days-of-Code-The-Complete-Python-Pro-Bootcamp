from flask import Flask
import random

guess = random.randint(0, 9)
print(guess)
app = Flask(__name__)


@app.route('/')
def home():
    return f'<h1>Guess a number between 0 & 9</h1><br><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def the_guess(number):
    if guess < number:
        return '<h1>Too high ~ try again, buddy. </h1><br><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess > number:
        return '<h1>Too Low ~ try again, buddy. </h1><br><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess == number:
        return '<h1>You found me, buddy. </h1><br><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    
    
if __name__ == '__main__':
    app.run(debug= True)
