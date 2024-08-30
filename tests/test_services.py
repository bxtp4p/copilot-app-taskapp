import unittest
from unittest.mock import patch, MagicMock
from services import TaskService, TaskValidation

class TestTaskService(unittest.TestCase):

    @patch('services.Task')
    def test_get_all_tasks(self, mock_Task):
        mock_Task.query.all.return_value = ['task1', 'task2']
        tasks = TaskService.get_all_tasks()
        self.assertEqual(tasks, ['task1', 'task2'])

    @patch('services.Task')
    def test_get_task_by_id(self, mock_Task):
        mock_Task.query.get.return_value = 'task'
        task = TaskService.get_task_by_id(1)
        self.assertEqual(task, 'task')

    @patch('services.db.session')
    @patch('services.Task')
    def test_add_task(self, mock_Task, mock_session):
        TaskService.add_task('title', 'description', False)
        mock_session.add.assert_called()
        mock_session.commit.assert_called()

    @patch('services.db.session')
    def test_update_task(self, mock_session):
        mock_task = MagicMock()
        updated_task = TaskService.update_task(mock_task, 'new title', 'new description', True)
        self.assertEqual(updated_task.title, 'new title')
        self.assertEqual(updated_task.description, 'new description')
        self.assertTrue(updated_task.done)
        mock_session.commit.assert_called()

    @patch('services.db.session')
    def test_delete_task(self, mock_session):
        mock_task = MagicMock()
        deleted_task = TaskService.delete_task(mock_task)
        mock_session.delete.assert_called_with(mock_task)
        mock_session.commit.assert_called()
        self.assertEqual(deleted_task, mock_task)
        
    # Unit test for adding a task without a title
    @patch('services.db.session')
    def test_add_task_no_title(self, mock_session):
        with self.assertRaises(ValueError) as context:
            TaskService.add_task('', 'description', False)
        self.assertEqual(str(context.exception), 'Task title is required')
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()
        
    # Unit test for adding a task with a title that is too long (over 255 characters)
    @patch('services.db.session')
    def test_add_task_title_too_long(self, mock_session):
        with self.assertRaises(ValueError) as context:
            TaskService.add_task('a' * 256, 'description', False)
        self.assertEqual(str(context.exception), 'Task title must be 255 characters or less')
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()
        
    # Unit test for a task with a description that is too long (over 1000 characters)
    @patch('services.db.session')
    def test_add_task_description_too_long(self, mock_session):
        with self.assertRaises(ValueError) as context:
            TaskService.add_task('title', 'a' * 1001, False)
        self.assertEqual(str(context.exception), 'Task description must be 1000 characters or less')
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()
        
    # Unit test for updating a task with a title that is too long (over 255 characters)
    @patch('services.db.session')
    def test_update_task_title_too_long(self, mock_session):
        mock_task = MagicMock()
        with self.assertRaises(ValueError) as context:
            TaskService.update_task(mock_task, 'a' * 256, 'description', False)
        self.assertEqual(str(context.exception), 'Task title must be 255 characters or less')
        mock_session.commit.assert_not_called()
        
    # Unit test for updating a task with a description that is too long (over 1000 characters)
    @patch('services.db.session')
    def test_update_task_description_too_long(self, mock_session):
        mock_task = MagicMock()
        with self.assertRaises(ValueError) as context:
            TaskService.update_task(mock_task, 'title', 'a' * 1001, False)
        self.assertEqual(str(context.exception), 'Task description must be 1000 characters or less')
        mock_session.commit.assert_not_called()
        
    # Unit test for updating a task with an empty title
    @patch('services.db.session')
    def test_update_task_no_title(self, mock_session):
        mock_task = MagicMock()
        with self.assertRaises(ValueError) as context:
            TaskService.update_task(mock_task, '', 'description', False)
        self.assertEqual(str(context.exception), 'Task title is required')
        mock_session.commit.assert_not_called()
        
    # Unit test for retrieving a task by a non-existent ID
    @patch('services.Task')    
    def test_get_task_by_id_not_found(self, mock_Task):
        mock_Task.query.get.return_value = None
        task = TaskService.get_task_by_id(1)
        self.assertIsNone(task)
        mock_Task.query.get.assert_called_with(1)
        mock_Task.query.get.assert_called_once()
        
class TestTaskValidation(unittest.TestCase):
    def test_validate_title_with_no_title(self):
        with self.assertRaises(ValueError) as context:
            TaskValidation.validate_title('')
        self.assertEqual(str(context.exception), 'Task title is required')

    def test_validate_title_with_long_title(self):
        with self.assertRaises(ValueError) as context:
            TaskValidation.validate_title('a' * 256)
        self.assertEqual(str(context.exception), 'Task title must be 255 characters or less')

    def test_validate_description_with_long_description(self):
        with self.assertRaises(ValueError) as context:
            TaskValidation.validate_description('a' * 1001)
        self.assertEqual(str(context.exception), 'Task description must be 1000 characters or less')
        
        