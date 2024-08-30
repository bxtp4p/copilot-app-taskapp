import unittest
from flask import json
from app import app
from extensions import db

class FunctionalTest(unittest.TestCase):
   def setUp(self):
      self.app = app.test_client()
      self.app.testing = True
      with app.app_context():
         # Setup a test database, if necessary
         db.create_all()

   def tearDown(self):
      with app.app_context():
         # Teardown the test database, if necessary
         db.session.remove()
         db.drop_all()

   def test_get_tasks(self):
      response = self.app.get('/')
      self.assertEqual(response.status_code, 200)
      # Additional assertions on the response data can be made here

   def test_add_task(self):
      response = self.app.post('/add', data=dict(title="Test Task", description="Test Description"), follow_redirects=True)
      self.assertEqual(response.status_code, 200)
      
      # Verify the task was added to the database
      response = self.app.get('/edit/1')
      self.assertEqual(response.status_code, 200)

   # Add more tests as needed for other endpoints
   def test_get_task(self):
      # make sure there is a task in the database
      self.app.post('/add', data=dict(title="Test Task", description="Test Description"), follow_redirects=True)
               
      response = self.app.get('/edit/1')
      self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()