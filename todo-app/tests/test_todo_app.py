
import unittest
from todo_app import TodoApp

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.todo_app = TodoApp()

    def test_add_task(self):
        self.todo_app.add_task("Buy milk")
        tasks = self.todo_app.get_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertIn("Buy milk", tasks)

    def test_remove_task(self):
        self.todo_app.add_task("Study Python")
        self.todo_app.remove_task(0)
        tasks = self.todo_app.get_tasks()
        self.assertEqual(len(tasks), 0)

    def test_update_task(self):
        self.todo_app.add_task("Write code")
        self.todo_app.update_task(0, "Finish project")
        tasks = self.todo_app.get_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertIn("Finish project", tasks)

if __name__ == '__main__':
    unittest.main()
