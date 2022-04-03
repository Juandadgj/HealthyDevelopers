from flask import Flask
from .config.database.database import configDatabase, db
from .routes.indexRoutes import configRoutes

app = Flask(__name__)

configDatabase()
db.create_all()

configRoutes()

if __name__ == '__main__':
    app.run()
