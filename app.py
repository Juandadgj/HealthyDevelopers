from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://juandadgj:JdGj1100080400@healthydevelopers.cvoacfqtexlc.us-east-2.rds.amazonaws.com/healthydevelopers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# mysql+pymysql://root:JdGj1100080400@localhost/healthy_developers
# mysql+pymysql://juandadgj:JdGj1100080400@healthydevelopers.cvoacfqtexlc.us-east-2.rds.amazonaws.com/healthydevelopers
# mysql://b6f8189f16420f:08256ce0@us-cdbr-east-03.cleardb.com/heroku_81bb379d58fee0e

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

db.create_all()

class UserSchema(mar.Schema):
    class Meta:
        fields = ('id', 'name', 'last_name', 'sex', 'mail', 'password', 'phone', 'direction')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

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

if __name__ == '__main__':
    app.run()
