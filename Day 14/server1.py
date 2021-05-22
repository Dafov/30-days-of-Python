from flask import Flask
from scrape import  run as scrape_runner
from logger import trigger_log_save

from waitress import serve


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "A very simple flask server!"

@app.route("/abc", methods=['GET'])
def abc_view():
    # run other code here.
    return "Hello, world. this is abc"

@app.route("/box-office-mojo-scraper", methods=['POST'])
def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {"data": [1,2,3]}

if __name__ == "__main__":
    serve(app, listen='*:8000')