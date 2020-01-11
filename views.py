from app import app,api, db
from flask_restplus import Resource, fields
from models import Todo, TodoSchema

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

@app.before_first_request
def create_tables():
    db.create_all()

# namespaces organise REST endpoints
ns_todos = api.namespace('todos', description='Todos Operations')

todos_model = api.model('Todo', {
    'title':fields.String,
    'description':fields.String
    
})

@ns_todos.route('')
class TodoList(Resource):
    def get(self):
        pass

    def post(self):
        pass

@ns_todos.route('/<int:id>')
class Todo(Resource):
    def get(self, id):
        pass
    
    def put(self, id):
        pass

    def delete(self, id):
        pass
