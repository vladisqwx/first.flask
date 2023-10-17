import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/index")
def main_func():
    return "this is a mfdfain page!"
@app.route("/birthday")
def main_func():
    return "My Birthday is November 25"
@app.route("/name")
def main_func():
    return "My Name Vladislav Osypchuk"
@app.route("/hobby")
def main_func():
    return "My hobby is playing piano"



if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))