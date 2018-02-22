from StravaWindAnalysisML.supervised import linear_regression as linReg
import unittest

class TestLinearRegression(unittest.TestCase):
    def test_modelRegression(self):
        data = "1|2|3|4|5|6|7|8"
        ans = "1.0|2.0|3.0|4.0|5.0|6.0|7.0|8.0"
        self.assertEqual(linReg.modelRegression(data), ans)

if __name__ == '__main__':
    unittest.main()
