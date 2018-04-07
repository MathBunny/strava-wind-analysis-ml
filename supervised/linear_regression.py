from sklearn import linear_model

def modelRegression(data):
    y_arr = data.split('|')

    x_arr = []
    for x in range(0, len(y_arr)):
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

    # Create line of best fit, y = mx + b
    ans = []
    for x in range(0, len(y_arr)):
        ans.append(float(m[0] * x + b))

    return '|'.join(str(v) for v in ans)


def regularizeData(speed_data):
    # Step #1: Run linear regression on speed data to regularize data
    y_arr = speed_data.split('|')

    x_arr = []
    for x in range(0, len(y_arr)):
        x_arr.append(x)

    speeds_x_train = x_arr
    speeds_y_train = y_arr

    speeds_x_train = map(lambda x: [x], speeds_x_train)
    speeds_y_train = map(lambda x: [x], speeds_y_train)

    regr = linear_model.LinearRegression()
    regr.fit(speeds_x_train, speeds_y_train)

    m = regr.coef_[0]
    b = regr.intercept_

    speeds = map(lambda x: float(x), speed_data.split('|'))

    # Step #2: Regularize data
    for x in range(0, len(speeds)):
        val = x * m + b
        diff = b - val
        speeds[x] = speeds[x] + diff

    return speeds


def windRegression(speed_data, correlationData, candidate):
    # Run linear regression on speed data to regularize data
    speeds = regularizeData(speed_data)
    correlations = correlationData.split('|')
    # Schwartzian Transform
    correlations, speeds = zip(*sorted(zip(correlations, speeds)))
    correlations, speeds = (list(t) for t in zip(*sorted(zip(correlations, speeds))))

    correlation_x_train = correlations
    speeds_y_train = speeds

    correlation_x_train = map(lambda x: [x], correlation_x_train)
    speeds_y_train = map(lambda x: [x], speeds_y_train)

    regr = linear_model.LinearRegression()
    regr.fit(correlation_x_train, speeds_y_train)

    m = regr.coef_[0]
    b = regr.intercept_

    return b + m * candidate.split('|')[1]


# print modelRegression("1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1")
