
import unittest
from todo_app import app

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        data = {'task': 'Test task'}
        response = self.app.post('/todo', json=data)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
