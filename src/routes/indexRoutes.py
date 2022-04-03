from flask import jsonify
from ..app import app
from ..controller.userController import *
from ..controller.habitController import *
from ..controller.progressController import *

def configRoutes():

    @app.route('/', methods=['GET'])
    def index():
        return jsonify(message="Welcome to our API")

    @app.route('/users', methods=['GET'])
    def getUserRoutes():
        getUsers()

    @app.route('/users/<mail>', methods=['GET'])
    def getUserRoute(mail):
        getUser(mail)

    @app.route('/users', methods=['POST'])
    def createUserRoute():
        createUser()

    @app.route('/users/<mail>', methods=['PUT'])
    def updateUserRoute(mail):
        updateUser(mail)

    @app.route('/users/<mail>', methods=['DELETE'])
    def deleteUserRoute(mail):
        deleteUser(mail)
    
    @app.route('/login/mail=<mail>&password=<password>', methods=['GET'])
    def loginRoute(mail, password):
        login(mail, password)
    
    @app.route('/habits', methods=['GET'])
    def getHabitsRoute():
        getHabits()

    @app.route('/progress/<mail>', methods=['GET'])
    def getProgressRoute(mail):
        getProgress(mail)

    @app.route('/progress', methods=['POST'])
    def createProgressRoute():
        createProgress()

    @app.route('/progress', methods=['PATCH'])
    def updateProgressRoute():
        updateProgress()

    @app.route('/progress/<mail>', methods=['DELETE'])
    def deleteProgressRoute(mail):
        deleteProgress(mail)