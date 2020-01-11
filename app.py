from flask import Flask
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import *

app = Flask(__name__)

app.config.from_object(Development)

api = Api(app=app, version='1.0', title='Todos API', description='An API to manage tasks')
db = SQLAlchemy(app)
ma = Marshmallow(app)


from views import *

if __name__ == "__main__":
    app.run()
