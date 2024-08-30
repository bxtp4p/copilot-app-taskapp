import unittest
from models import Task

class TestTaskModel(unittest.TestCase):
    def test_repr_method(self):
        # Create a Task instance with specific attributes
        task = Task(id=1, title='Test Task', description='Test Description', done=False)
        
        # Expected representation
        expected_repr = "<Task Test Task>"
        
        # Assert that the __repr__ method returns the expected string
        self.assertEqual(repr(task), expected_repr)

if __name__ == '__main__':
    unittest.main()