from flask_restplus import Resource, fields
from werkzeug.exceptions import BadRequest

from app import app,api, db
from models.todo import Todo, TodoSchema

from datetime import datetime


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

@app.before_first_request
def create_tables():
    db.create_all()

# namespaces organise REST endpoints
ns_todos = api.namespace('todos', description='Todos Operations')

todo_model = api.model('Todo', {
    'title':fields.String,
    'description':fields.String
    
})

@ns_todos.route('')
class TodoList(Resource):
    @api.doc('list_todos', responses={ 200: 'OK', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })    
    def get(self):
        '''List all todos'''
        try:
            my_todos = Todo.fetch_all() 
            todos = todos_schema.dump(my_todos)
            return {'status':'Matches retrieved', 'todos':todos}, 200
        except KeyError as e:
            ns_todos.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            ns_todos.abort(400, e.__doc__, status = "Could perform this action", statusCode = "400")
        
    @api.doc('post_todo', responses={ 200: 'OK', 201:'Created', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })    
    @api.expect(todo_model)
    def post(self):
        '''Post todo item to database'''
        try:
            data = api.payload
            new_todo = Todo(title=data['title'], description=data['description'])
            new_todo.insert_record()
            todo = todo_schema.dump(data)
            return {'status':'Todo item added', 'todo':todo}, 201
        except KeyError as e:
            ns_todos.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            ns_todos.abort(400, e.__doc__, status = "Could not perform this action", statusCode = "400")

@ns_todos.route('/<int:id>')
@ns_todos.param('id', 'The todo item identifier')
class TodoItem(Resource):
    @api.doc('get_todo', responses={ 200: 'OK', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })
    def get(self, id):
        try:
            my_todo = Todo.fetch_by_id(id)
            todo = todo_schema.dump(my_todo)
            if len(todo) == 0:
                e = BadRequest('Todo item does not exist')
                e.data = {'status':'404'}
                raise e
            return {'status':'Match retrieved', 'todo':todo}, 200
        except KeyError as e:
            ns_todos.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
        except Exception as e:
            ns_todos.abort(404, e.__doc__, status = "Todo item does not exist", statusCode = "404")
    
    @api.doc('edit_todo', responses={ 200: 'OK', 201:'Created', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })
    @api.expect(todo_model)
    def put(self, id):
        '''Edit todo item in database'''
        try:
            data = api.payload
            
            id=id
            title = data['title']
            description = data['description']
            updated = datetime.utcnow()
            Todo.update_todo(id=id, title=title,  description=description, updated=updated)
            todo = todo_schema.dump(data)
            return {'status':'Todo item has been updated', 'todo':todo}, 201
        except KeyError as e:
            ns_todos.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            ns_todos.abort(400, e.__doc__, status = "Could not perform this action", statusCode = "400")
    
    @api.doc('delete_todo', responses={ 200: 'OK', 201:'Created', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })
    def delete(self, id):
        '''Delete todo item from database'''
        try:
            Todo.delete_by_id(id)
            return {'status':'Todo item has been deleted'}
        except KeyError as e:
            ns_todos.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            ns_todos.abort(400, e.__doc__, status = "Could perform this action", statusCode = "400")

