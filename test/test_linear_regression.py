from StravaWindAnalysisML.supervised import linear_regression as linReg
import unittest

class TestLinearRegression(unittest.TestCase):
    def test_modelRegressionLinearPositive(self):
        data = "1|2|3|4|5|6|7|8"
        ans = "1.0|2.0|3.0|4.0|5.0|6.0|7.0|8.0"
        self.assertEqual(linReg.modelRegression(data), ans)

    def test_modelRegressionLinearNegative(self):
        data = "1|0|-1|-2"
        ans = "1.0|0.0|-1.0|-2.0"
        self.assertEqual(linReg.modelRegression(data), ans)

    def test_modelRegressionSingle(self):
        data = "1"
        ans = "1.0"
        self.assertEqual(linReg.modelRegression(data), ans)

    def test_modelRegressionConstant(self):
        data = "1|1|1|1|1|1|1|1"
        ans = "1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0"
        self.assertEqual(linReg.modelRegression(data), ans)

    def test_modelRegressionSinusoidal(self):
        data = "1|2|1|0|1"
        ans = "1.4|1.2|1.0|0.8|0.6"
        self.assertEqual(linReg.modelRegression(data), ans)

if __name__ == '__main__':
    unittest.main()
