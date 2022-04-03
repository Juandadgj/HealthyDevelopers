from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ...app import app
from ..env.envModule import configEnv

def configDatabase():
    
    app.config['SQLALCHEMY_DATABASE_URI'] = configEnv['DB_MYSQL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
mar = Marshmallow(app)
