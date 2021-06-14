from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b694ff5d16630d:d6ef68c2@us-cdbr-east-03.cleardb.com/heroku_f6deb47a67d65f8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# mysql+pymysql://root:JdGj1100080400@localhost/healthy_developers
# mysql+pymysql://b694ff5d16630d:d6ef68c2@us-cdbr-east-03.cleardb.com/heroku_f6deb47a67d65f8

db = SQLAlchemy(app)
mar = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    mail = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(15))
    direction = db.Column(db.String(100))

    def __init__(self, name, last_name, sex, mail, password, phone, direction):
        self.name = name
        self.last_name = last_name
        self.sex = sex
        self.mail = mail
        self.password = password
        self.phone = phone
        self.direction = direction

class Habit(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(45), nullable=False)

    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category

class Progress(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    usermail = db.Column(db.String(255), nullable=False)
    habitid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, usermail, habitid, status):
        self.usermail = usermail
        self.habitid = habitid
        self.status = status

db.create_all()

class UserSchema(mar.Schema):
    class Meta:
        fields = ('id', 'name', 'last_name', 'sex', 'mail', 'password', 'phone', 'direction')

class HabitSchema(mar.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'category')

class ProgressSchema(mar.Schema):
    class Meta:
        fields = ('id', 'usermail', 'habitid', 'status')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
habit_schema = HabitSchema()
habits_schema = HabitSchema(many=True)
progress_schema = ProgressSchema()
progresess_schema = ProgressSchema(many=True)

@app.route('/', methods=['GET'])
def index():
    return jsonify(message="Welcome to our API")

@app.route('/users', methods=['POST'])
def create_user():
    name = request.json['name']
    last_name = request.json['last_name']
    sex = request.json['sex']
    mail = request.json['mail']
    password = request.json['password']
    phone = request.json['phone']
    direction = request.json['direction']

    new_user = User(name, last_name, sex, mail, password, phone, direction)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route('/users/<mail>', methods=['GET'])
def get_user(mail):
    user = User.query.filter_by(mail=mail).first()
    print(user)
    return user_schema.jsonify(user)

@app.route('/users/<mail>', methods=['PUT'])
def update_user(mail):
    user = User.query.filter_by(mail=mail).first()
    name = request.json['name']
    last_name = request.json['last_name']
    sex = request.json['sex']
    mail = request.json['mail']
    password = request.json['password']
    phone = request.json['phone']
    direction = request.json['direction']

    user.name = name
    user.last_name = last_name
    user.sex = sex
    user.mail = mail
    user.password = password
    user.phone = phone
    user.direction = direction

    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/users/<mail>', methods=['DELETE'])
def delete_user(mail):
    user = User.query.filter_by(mail=mail).first()
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/login/mail=<mail>&password=<password>', methods=['GET'])
def login(mail, password):
    user = User.query.filter_by(mail=mail).first()
    if user.password == password:
        return jsonify(message="Correct")
    else:
        return jsonify(message="Incorrect")

@app.route('/habits', methods=['GET'])
def get_habits():
    all_habits = Habit.query.all()
    result = habits_schema.dump(all_habits)
    return jsonify(result)

@app.route('/progress/<mail>', methods=['GET'])
def get_progress(mail):
    progress = Progress.query.filter_by(usermail=mail)
    result = progresess_schema.dump(progress)
    return jsonify(result)

@app.route('/progress', methods=['POST'])
def create_progress():
    usermail = request.json['usermail']
    habitid = request.json['habitid']
    status = request.json['status']

    new_progress = Progress(usermail, habitid, status)
    db.session.add(new_progress)
    db.session.commit()
    return progress_schema.jsonify(new_progress)

@app.route('/progress', methods=['PATCH'])
def update_progress():
    mail = request.json['usermail']
    habitid = request.json['habitid']
    progress = Progress.query.filter_by(usermail=mail, habitid=habitid).first()
    status = request.json['status']
    progress.status = status
    db.session.commit()
    return progress_schema.jsonify(progress)

@app.route('/progress/<mail>', methods=['DELETE'])
def delete_progress(mail):
    mail = mail
    progress = Progress.query.filter_by(usermail=mail).order_by(Progress.id.desc()).first()
    db.session.delete(progress)
    db.session.commit()
    return progress_schema.jsonify(progress)

if __name__ == '__main__':
    app.run()
