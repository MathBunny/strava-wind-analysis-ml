# Strava Wind Analysis - ML Backend

The purpose of this RESTful API is to perform machine learning analytics on cycling data.


This server provides basic ordinary linear regression for time-speed graphs and clustering using k-means for aggregate ride speed-distance graphs. 


The server also provides machine learning for wind correlation determination. First, regularization runs on historic segment efforts to prevent the data from being skewed from the athlete improving or getting worse over time. After, regression on several features including wind-speed, wind-direction is executed. Finally, it takes the post-processed correlation determined through the vector manipulation algorithm computed from the Node server.

Please consult the official [Strava Wind Analysis repository](https://github.com/MathBunny/strava-wind-analysis) for the site itself.


## Running the server
Ensure that you have `scikit-learn` installed, along with `Python 3.x`. 

To start the server, run:
```
FLASK_APP=app.py flask run
```

## Endpoints
```
/get/linear-regression/<string:data>
Expected format:
a|b|c|d  -- where a,..,d = floating numbers representing speed
```

```
/get/wind-regression/<string:data>
Expected format:
a|b|c|d&e|f|g  -- where a,..,d = floating numbers representing speed, e, ..., g = floating numbers representing post-processed wind/speed correlation
```

```
/get/kmeans-rides-clustering/<string:data>
Expected format:
a,b|c,d|e,f|g,h|i,j -- where a,b is the (x,y) tuple on the graph and | is the seperation between activities
```

The server should be listening on `http://127.0.0.1:5000/`