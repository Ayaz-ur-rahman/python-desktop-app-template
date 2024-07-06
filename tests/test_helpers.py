import unittest
from app.utils.helpers import example_helper_function

class TestHelpers(unittest.TestCase):
    def test_example_helper_function(self):
        self.assertIsNone(example_helper_function())

if __name__ == "__main__":
    unittest.main()
