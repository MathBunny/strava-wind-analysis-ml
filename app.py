from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Welcome to the Strava Wind Analysis Machine Learning Backend."

@app.errorhandler(404)
def page_not_found(error):
    return "Error: Not Found!", 404

@app.route("/get/linear-regression/<string:data>")
def compute(data):
  return data