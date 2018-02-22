from StravaWindAnalysisML.unsupervised import kmeans_rides as kmeansRides
import unittest

class TestRidesClustering(unittest.TestCase):
    def test_threeclusters(self):
        data = "1,1|2,2|4,4|6,6|32132,13231|33443,3432|-322,-32123|-321,-43211"
        ans = "2|2|2|2|0|0|1|1"
        self.assertEqual(kmeansRides.clusterActivities(data, 3), ans)

    def test_singlecluster(self):
        data = "1,1|2,2|4,4|6,6|32132,13231|33443,3432|-322,-32123|-321,-43211"
        ans = "0|0|0|0|0|0|0|0"
        self.assertEqual(kmeansRides.clusterActivities(data, 1), ans)

    def test_singlepoint(self):
        data = "1,1"
        ans = "0"
        self.assertEqual(kmeansRides.clusterActivities(data, 1), ans)

    def test_singlepointTwoClusters(self):
        data = "1,1|2,2"
        ans = "0|1"
        self.assertEqual(kmeansRides.clusterActivities(data, 2), ans)

if __name__ == '__main__':
    unittest.main()
