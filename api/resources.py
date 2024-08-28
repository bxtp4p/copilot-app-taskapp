from flask import Blueprint
from flask import jsonify
from flask_restful import Api, Resource
from models import Task
from services import TaskService

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

class TaskList(Resource):
    def get(self):
        tasks = TaskService.get_all_tasks()
        return jsonify([{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        } for task in tasks])

class TaskResource(Resource):    
    def get(self, task_id):
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
        pass
        

    def put(self, task_id):
        # Logic to update an item
        pass

    def delete(self, task_id):
        # Logic to delete an item
        pass

api.add_resource(TaskList, '/tasks')
api.add_resource(TaskResource, '/task/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)