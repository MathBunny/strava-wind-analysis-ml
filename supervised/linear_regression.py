from sklearn import linear_model

def modelRegression(data):
    # speeds = np.fromstring(str, dtype=float, sep="|")
    y_arr = data.split('|')

    x_arr = []
    for x in range (0, len(y_arr)):
        x_arr.append(x)

    speeds_x_train = x_arr
    speeds_y_train = y_arr

    speeds_x_train = map(lambda x: [x], speeds_x_train)
    speeds_y_train = map(lambda x: [x], speeds_y_train)

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(speeds_x_train, speeds_y_train)

    m = regr.coef_[0]
    b = regr.intercept_

    # Create line of best fit
    ans = []
    for x in range(0, len(y_arr)):
        ans.append(float(m[0] * x + b))

    return '|'.join(str(v) for v in ans)

# modelRegression("1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1")
