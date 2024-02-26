import random
import unittest
from time import perf_counter as current_time
from prog985t import Mergesort

class TestMergesort(unittest.TestCase):
    # Test with a typical list of numbers
    def test_normal_case(self):
      input = [4, 2, 5, 1, 3]
      expected_output = [1, 2, 3, 4, 5]
      self.assertEqual(Mergesort.sort(input), expected_output)

    # Test with an empty list
    def test_empty_list(self):
      input = []
      expected_output = []
      self.assertEqual(Mergesort.sort(input), expected_output)

    # Test with a list having one element
    def test_single_element(self):
      input = [1]
      expected_output = [1]
      self.assertEqual(Mergesort.sort(input), expected_output)

    # Test with a list where all elements are identical
    def test_identical_elements(self):
      input = [5, 5, 5, 5]
      expected_output = [5, 5, 5, 5]
      self.assertEqual(Mergesort.sort(input), expected_output)

    # Test with negative numbers in the list
    def test_negative_numbers(self):
      input = [-3, -1, -4, -2]
      expected_output = [-4, -3, -2, -1]
      self.assertEqual(Mergesort.sort(input), expected_output)

    # Test with mixed integer and float values
    def test_mixed_types(self):
      input = [3.2, 1.5, 4.8, 2.1]
      expected_output = [1.5, 2.1, 3.2, 4.8]
      self.assertEqual(Mergesort.sort(input), expected_output)

    # (Optional) Test for performance on a large dataset
    def test_performance_large_dataset(self):
      input = generate_large_random_list()
      start_time = current_time()
      Mergesort.sort(input)
      end_time = current_time()
      self.assertLess(end_time-start_time, 10)# try 10 seconds

# Helper function to generate a large random list
def generate_large_random_list():
  return [random.randint(0, 10_000_000) for i in range(1_000_000)]

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestMergesort)
  unittest.TextTestRunner(verbosity=0).run(suite)
