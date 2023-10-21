import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def main_func():
    return render_template("base.html")

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

