import os
from flask import Flask, render_template
from dotenv import load_dotenv
from enums import NAME, MAX_SCORE, students
load_dotenv()

app = Flask(__name__)

@app.route("/")
def main_func():
    return render_template("index.html", title="Title test")
@app.route("/context")
def context_return():
    context = {
        "title": "Python course ",
        "students": students,
        "name": NAME,
        "max_score": MAX_SCORE
    }
    return render_template("context.html", **context)
@app.route("/birthday")
def main_func1():
    return "My Birthday is November 25"
@app.route("/name")
def main_func2():
    return "My Name Vladislav Osypchuk"
@app.route("/hobby")
def main_func3():
    return "My hobby is playing piano!"

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))

