from flask import Flask


app = Flask(__name__)

@app.route("/index")
def main_func():
    return "this is a main page!"


if __name__ == "__main__":
    app.run(debug=True)