from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from models import Task
from services import TaskService

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

class TaskList(Resource):
    """
    Resource for listing all tasks and adding a new task.
    """

    def get(self):
        """
        Retrieve a list of all tasks.

        Returns:
        - JSON representation of all tasks.
        """
        tasks = TaskService.get_all_tasks()
        return jsonify([{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        } for task in tasks])

class TaskResource(Resource):
    """
    Resource for getting, updating, and deleting a single task.
    """

    def get(self, task_id):
        """
        Retrieve a single task by its ID.

        Parameters:
        - task_id: ID of the task to retrieve.

        Returns:
        - JSON representation of the task if found.
        - 404 error if the task is not found.
        """
        task = TaskService.get_task_by_id(task_id)
        if task:
            return jsonify({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'done': task.done
            })
        else:
            return {'message': 'Task not found'}, 404

    def post(self):
        """
        Add a new task. The implementation is not provided here.
        """
        pass

    def put(self, task_id):
        """
        Update an existing task. The implementation is not provided here.

        Parameters:
        - task_id: ID of the task to update.
        """
        pass

    def delete(self, task_id):
        """
        Delete an existing task. The implementation is not provided here.

        Parameters:
        - task_id: ID of the task to delete.
        """
        pass

# Registering resources with the API
api.add_resource(TaskList, '/tasks')
api.add_resource(TaskResource, '/task/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)