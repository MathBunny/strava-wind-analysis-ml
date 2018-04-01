import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from coordinate_utils import bearing_to_vector

training_data = []
cross_validation = []
test_data = []
clf = MLPRegressor(hidden_layer_sizes=(4, ), activation='relu',
                   solver='sgd', alpha=0.0001, batch_size='auto',
                   learning_rate='adaptive', learning_rate_init=0.001,
                   power_t=0.5, max_iter=50000, shuffle=True, random_state=None,
                   tol=0.0001, verbose=False, warm_start=False, momentum=0.9,
                   nesterovs_momentum=True, early_stopping=False,
                   validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
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
    test_data = data[int(num_lines * 0.7):] #0.7

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

    clf.fit(X_train, y_train)

def test():
    xy_vals = get_xy_vals(test_data)
    X_test = xy_vals[0]
    y_test = xy_vals[1]
    X_test = scaler.transform(X_test)
    y_pred = clf.predict(X_test)

    for x in range(len(X_test)):
        print str(round(y_pred[x], 2)) + 'km/h vs ' + str(round(y_test[x], 2)) + 'km/h'

    print 'R^2 =', clf.score(X_test, y_test, None)
    print 'Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred))

    #for x in range(len(X_test)):
        #print X_test[x]

load_data()
train()
test()
