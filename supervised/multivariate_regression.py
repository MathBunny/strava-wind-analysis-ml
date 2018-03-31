import numpy as np
# from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn import metrics    
from coordinate_utils import bearing_to_vector

training_data = []
cross_validation = []
test_data = []
# regressor = LinearRegression() # normalize=True
regressor = Ridge(alpha=.7)
scaler = StandardScaler()

def load_data():
    training_file = open('training.txt', 'r')

    num_lines = sum(1 for line in open('training.txt'))
    data = []
    for line in training_file:
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

        distance = float(data[1])
        moving_time = float(data[2])
        ride_bearing = float(data[3])
        avg_grade = float(data[4])
        wind_speed = float(data[5])
        wind_bearing = float(data[6])

        ride_vector = bearing_to_vector(ride_bearing)
        wind_vector = bearing_to_vector(wind_bearing)

        speed = (distance * 3.6) / moving_time
        features = []
        features.append(distance)

        dx = abs(ride_vector[0] + wind_vector[0])
        dy = abs(ride_vector[1] + wind_vector[1])
        add = abs(ride_vector[0]) + abs(ride_vector[1])
        
        features.append((dx + dy - add) * wind_speed)

        # print (dx + dy - add) * wind_speed
        features.append(avg_grade)

        X_train.append(features)
        y_train.append(speed)

    return (X_train, y_train)

def train():
    xy_vals = get_xy_vals(training_data)
    X_train = xy_vals[0]
    y_train = xy_vals[1]

    scaler.fit(X_train)
    X_train = scaler.transform(X_train)

    regressor.fit(X_train, y_train)

def test():
    xy_vals = get_xy_vals(test_data)
    X_test = xy_vals[0]
    y_test = xy_vals[1]
    X_test = scaler.transform(X_test)
    y_pred = regressor.predict(X_test)

    for x in range(len(X_test)):
        print str(round(y_pred[x], 2)) + 'km/h vs ' + str(round(y_test[x], 2)) + 'km/h'

    print 'Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)) 
    print 'Coefficients: ', regressor.coef_
    print 'Intercept: ', regressor.intercept_

    # for x in range(len(X_test)):
        # print X_test[x][1], X_test[x]

load_data()
train()
test()