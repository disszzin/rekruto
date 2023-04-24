from flask import request, render_template
import re
from app import app

@app.route("/")
def mainView():
    '''The main view for the output of this beautiful task :)'''
    name = request.args.get("name", "Rekruto!")
    message = request.args.get("message", "Давай дружить!")

    return render_template("index.html", name=checkCorrect(name), message=checkCorrect(message))

def checkCorrect(text: str) -> str:
    '''Func for check exclamation mark, i dont know why, but, will be ¯\_(ツ)_/¯'''
    pattern = r"^\w+.*!"
    if re.match(pattern=pattern, string=text):
        return text
    return text + "!"
