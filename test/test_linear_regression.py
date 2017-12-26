from ..supervised import linear_regression as linReg
import unittest

class TestLinearRegression(unittest.TestCase):
    def test_modelRegression(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(linReg.modelRegression(data) == data)

if __name__ == '__main__':
    unittest.main()
