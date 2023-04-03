from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style=\'text-align: center\'>Guess a number between 0 and 9</h1>'\
           '<img style=\'display: block; margin-left: auto; margin-right: auto; width: 40%;\' ' \
           'src=\'https://media.giphy.com/media/8FxtdFhCKXLFTWkX1H/giphy.gif\' >'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img style=\'display: block; margin-left: auto; margin-right: auto; width: " \
               "40%;\'src='https://media.giphy.com/media/a7YZXgEkaYyWI/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img style=\'display: block; margin-left: auto; margin-right: auto; width: " \
               "40%;\'src='https://media.giphy.com/media/nRNF5nlDgr8bK/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img style=\'display: block; margin-left: auto; margin-right: auto; width: " \
               "40%;\'src='https://media.giphy.com/media/dxbPGFv7tSK3e/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)


