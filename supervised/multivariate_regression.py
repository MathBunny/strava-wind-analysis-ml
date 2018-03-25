import math
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics    
from coordinate_utils import *

training_data = []
cross_validation = []
test_data = []
regressor = LinearRegression()

def load_data():
    file = open('training.txt', 'r')

    num_lines = sum(1 for line in open('training.txt'))
    data = []
    for line in file:
        data.append(line)

    global training_data, cross_validation, test_data

    training_data = data[:int(num_lines * 0.7)]
    cross_validation = data[int(num_lines * 0.7):int(num_lines * 0.85)]
    test_data = data[int(num_lines * 0.7):]

def get_xy_vals(arr):
    X_train = []
    y_train = []

    for line in arr:
        data = line.split(',')
        id = data[0]
        distance = float(data[1])
        moving_time = float(data[2])
        ride_bearing = float(data[3])
        wind_speed = float(data[4])
        wind_bearing = float(data[5])

        ride_vector = bearing_to_vector(ride_bearing)
        wind_vector = bearing_to_vector(wind_bearing)

        speed = (distance * 3.6) / moving_time
        features = []
        features.append(distance)
        features.append(wind_speed)
        features.append(ride_vector[0])
        features.append(ride_vector[1])
        features.append(wind_vector[0])
        features.append(wind_vector[1])
        X_train.append(features)
        y_train.append(speed)

    return (X_train, y_train)

def train():
    xy_vals = get_xy_vals(training_data)
    X_train = xy_vals[0]
    y_train = xy_vals[1]

    regressor.fit(X_train, y_train)

def test():
    xy_vals = get_xy_vals(test_data)
    X_test = xy_vals[0]
    y_test = xy_vals[1]
    y_pred = regressor.predict(X_test)

    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))  


load_data()
train()
test()