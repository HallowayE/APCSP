import random
import unittest
from time import perf_counter as current_time
from prog985a import Calc

""" 
Test each case with the following:
normal case: 1, 2
edge case: 0, 0
error case: 1, -1
"""

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = current_time()

    def tearDown(self):
        t = current_time() - self.startTime
        print(f"{self.id()}: {t:.6f}")

    def test_add_normal(self):
      self.assertEqual(Calc.add(1, 2), 3)
    def test_add_edge(self):
      self.assertEqual(Calc.add(0, 0), 0)
    def test_add_error(self):
      self.assertEqual(Calc.add(1, -1), 0)

    def test_sub_normal(self):
      self.assertEqual(Calc.sub(1, 2), -1)
    def test_sub_edge(self):
      self.assertEqual(Calc.sub(0, 0), 0)
    def test_sub_error(self):
      self.assertEqual(Calc.sub(1, -1), 2)

    def test_mul_normal(self):
      self.assertEqual(Calc.mul(1, 2), 2)
    def test_mul_edge(self):
      self.assertEqual(Calc.mul(0, 0), 0)
    def test_mul_error(self):
      self.assertEqual(Calc.mul(1, -1), -1)

    def test_div_normal(self):
      self.assertEqual(Calc.div(1, 2), 0.5)
    def test_div_edge(self):
      with self.assertRaises(ZeroDivisionError):
        Calc.div(0, 0)
    def test_div_error(self):
      self.assertEqual(Calc.div(1, -1), -1)

    def test_mod_normal(self):
      self.assertEqual(Calc.mod(1, 2), 1)
    def test_mod_edge(self):
      with self.assertRaises(ZeroDivisionError):
        Calc.mod(0, 0)
    def test_mod_error(self):
      self.assertEqual(Calc.mod(1, -1), 0)
      

    # def test_one(self):
    #     self.assertEqual(methodcall, expectedvalue)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)
    unittest.TextTestRunner(verbosity=0).run(suite)