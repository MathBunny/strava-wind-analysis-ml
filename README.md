# Strava Wind Analysis - ML Backend

The purpose of this RESTful API is to perform machine learning analytics on cycling data.


This server provides basic ordinary linear regression for time-speed graphs and clustering using k-means for aggregate ride speed-distance graphs. 

## Wind Correlation Determination Algorithm

There is also support with machine learning for wind correlation determination. First, standardization runs on historic segment efforts to prevent the data from being skewed from the athlete improving or getting worse over time. After, regression on several features including wind-speed, wind-direction is executed. Finally, it takes the post-processed correlation determined through the vector manipulation algorithm computed from the Node server.


## Neural Networks and Multivariate Linear Regression Model

A newer wind correlation determination algorithm uses multivariate linear regression with L2 regularization (ridge), and a 200 layer multilayer peceptron deep neural network using stochastic gradient descent. Both models use standardization on the data using a standard scaler. The features used are segment elevation change, ride distance, and a factor computed through vector manipulation.


Following a similar algorithm as used originally, the physics model first converts `lat`/`long` pairs of the ride start/end into bearing. Then, it converts the bearing into a unit vector. We perform the last step as well for the wind bearing. After, the `x` and `y` components are added, and then net change is observed relative to the ride direction vector. Next, we sum the relative change in the `x` and `y` axes, and multiply it by the wind speed.


The final result is used to determine the last feature in our labelled data-set. To determine the speed without wind, we would submit the same feature set to our model, but let the relative change feature be 0. This allows for us to use historical segment performance for our training set.


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
a|b|c|d&e|f|g&h|i  -- where a,..,d = floating numbers representing speed
                   -- where e,..., g = floating numbers representing post-processed wind/speed correlation
                   -- where h, i represent the speed and post-processed candidate wind/speed correlation respectively
```

```
/get/kmeans-rides-clustering/<string:data>
Expected format:
a,b|c,d|e,f|g,h|i,j -- where a,b is the (x,y) tuple on the graph and | is the seperation between activities
```

The server should be listening on `http://127.0.0.1:5000/`

## Tests

You can run tests as follows:
```shell
python -m StravaWindAnalysisML.test.test_linear_regression
python -m StravaWindAnalysisML.test.test_rides_clustering
```

## Utilities

You can also run several utilities included in the `/utils` folder. You should first create a file called `config.py` in the root of the `utils` folder:
```python
ACCESS_TOKEN=xyz
WEATHER_ACCESS_TOKEN=abc
```

Where `xyz` / `abc` = your access tokens respectively. You can then invoke the scripts to generate training data for your models quickly!