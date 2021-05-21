from flask import Flask
from waitress import serve


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:gray'> A very simple flask server !</h1>"

if __name__ == "__main__":
    serve(app, listen='*:8080')