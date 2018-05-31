from sklearn.cluster import KMeans
import numpy as np

# Data is expected as a,b|c,d|e,f|
def clusterActivities(data, num_clusters):
    input = data.split('|')

    if data == '':
        return ''
    num_clusters = min(len(input), num_clusters)

    arr = []
    for point in input:
        pointArr = point.split(',')
        arr.append((pointArr[0], pointArr[1]))

    X = np.array(arr)
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)
    return '|'.join(str(v) for v in np.array(kmeans.labels_).tolist())


# print clusterActivities('1,1|2,2|4,4|6,6|32132,13231|33443,3432|-322,-32123|-321,-43211', 3)