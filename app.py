from flask import Flask
from supervised import linear_regression as linReg
from unsupervised import kmeans_rides as kmeansRides
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the Strava Wind Analysis Machine Learning Backend."

@app.errorhandler(404)
def page_not_found(error):
    return "Error: Not Found!", 404

@app.route("/get/linear-regression/<string:data>")
def linRegression(data):
    return linReg.modelRegression(data)

@app.route("/get/wind-regression/<string:data>")
def windRegression(data):
    param = data.split('&')
    return linReg.windRegression(param[0], param[1], param[2])

@app.route("/get/kmeans-rides-clustering/<string:data>")
def kmeansClustering(data):
    param = data.split('&')
    return kmeansRides.clusterActivities(param[0], int(param[1]))
