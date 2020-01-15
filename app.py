from flask import Flask, Blueprint
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import *

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation', title='Todos API', version='1.0', description='An API to manage tasks')

app.register_blueprint(blueprint)

app.config.from_object(Development)

db = SQLAlchemy(app)
ma = Marshmallow(app)


from views import *

if __name__ == '__main__':
    app.run()