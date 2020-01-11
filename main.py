from flask import Flask
from flask_restplus import Resource, Api, fields

app = Flask(__name__)
api = Api(app=app, version='1.0', title='Todos API', description='An API to manage tasks')

# namespaces organise REST endpoints
ns_todos = api.namespace('todos', description='Todos Operations')

todos_db = [
    {'id':1,
        'title':'Cook',
        'description':'Cook ugali & meat'
    },
    {'id':2,
        'title':'Meeting',
        'description':'Techcamp Meeting'
    }
]

todos_model = api.model('Todo', {
    'title':fields.String,
    'description':fields.String
})

@ns_todos.route('')
class TodoList(Resource):
    @api.marshal_with(todos_model, envelope='todos')
    # get all todos
    def get(self):
        return todos_db, 200

    @api.expect(todos_model)
    def post(self):
        new_todo = api.payload
        new_todo['id'] = len(todos_db) + 1
        todos_db.append(new_todo)
        print('The payload: ', new_todo)
        return new_todo, 201

@ns_todos.route('/<int:id>')
class Todo(Resource):
    def get(self, id):
        
        get_item = filter(lambda my_todo: my_todo['id'] == id, todos_db)
        task = list(get_item)
        if len(task) == 0:
            return{'message':'Todo item does not exist'}, 404
        
        return task[0], 200
    
    @api.expect(todos_model)
    def put(self, id):
        get_item = filter(lambda my_todo: my_todo['id'] == id, todos_db)
        task = list(get_item)[0]
        payload = api.payload
        if 'title' in payload:
            task['title'] = payload['title']
        if 'title' in payload:  
            task['description'] = payload['description']
        return {'message':'Todo Item updated'}, 200

    def delete(self, id):
        print(todos_db)
        for i in range(len(todos_db)):
            if id == todos_db[i]['id']:
                todos_db.pop(i)
                return{'message':'Todo Item deleted'}, 200
                print(todos_db)
        


if __name__ == "__main__":
    app.run()
