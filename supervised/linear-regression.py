import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

def modelRegression(data):
    # speeds = np.fromstring(str, dtype=float, sep="|")
    y_arr = data.split('|')

    # Split the data into training/testing sets
    x_arr = []
    for x in range (0, len(y_arr)):
        x_arr.append(x)

    speeds_x_train = x_arr
    speeds_y_train = y_arr
    #speeds_x_test = x_arr[-20:]
    #speeds_y_test = speeds[-20:]

    speeds_x_train = map(lambda x: [x], speeds_x_train)
    speeds_y_train = map(lambda x: [x], speeds_y_train)

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(speeds_x_train, speeds_y_train)

    m = regr.coef_[0]
    b = regr.intercept_
    print(' y = {0} * x + {1}'.format(m, b))

    # Create line of best fit

    ans = []
    for x in range(0, len(y_arr)):
        ans.append(int(m[0] * x + b))

    return '|'.join(str(v) for v in ans)

modelRegression("1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1")