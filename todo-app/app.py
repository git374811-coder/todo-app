
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    def get(self, task_id):
        # Implement reading a specific task by ID
        pass

    def put(self, task_id):
        # Implement updating a specific task by ID
        pass

    def delete(self, task_id):
        # Implement deleting a specific task by ID
        pass

class TaskList(Resource):
    def get(self):
        # Implement reading all tasks
        pass

    def post(self):
        # Implement creating a new task
        pass

api.add_resource(Task, '/tasks/<int:task_id>')
api.add_resource(TaskList, '/tasks')

if __name__ == '__main__':
    app.run(debug=True)
