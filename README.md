# Strava Wind Analysis - ML Backend

The purpose of this RESTful API is to perform machine learning analytics on cycling data.


So far, this server only provides basic ordinary linear regression for time-speed graphs. More features will be added later. Please consult the official Strava Wind Analysis repository for the site itself.


## Running the server
Ensure that you have `scikit-learn` installed, along with `Python 3.x`. 

To start the server, run:
```
FLASK_APP=app.py flask run
```

The server should be listening on `http://127.0.0.1:5000/`.