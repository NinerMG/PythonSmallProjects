# advanced decorators
# rendering html
# parsing url
# flask debugging

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMml1MDhtNnpzb2ZsbDJhY2dwb2U0ZHc4bmxqYWd1NzMxZHVlYzVuNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gyRWkLSQVqlPi/giphy.gif" width=200>'
            '')

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)