
import unittest
from your_app import app, get_data

class TestApp(unittest.TestCase):
    def test_get_data(self):
        # Mocked data to test with
        mocked_data = {"key1": "value1", "key2": "value2"}
        
        # Act
        result = get_data()
        
        # Assert
        self.assertEqual(result, mocked_data)

if __name__ == '__main__':
    unittest.main()
