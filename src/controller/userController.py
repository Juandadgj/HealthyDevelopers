from flask import request, jsonify
from ..config.database.database import db
from ..model.User import User, user_schema, users_schema
from ..model.Progress import Progress

def createUser():
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

def getUsers():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

def getUser(mail):
    user = User.query.filter_by(mail=mail).first()
    print(user)
    return user_schema.jsonify(user)

def updateUser(mail):
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

def deleteUser(mail):
    user = User.query.filter_by(mail=mail).first()
    progresess = Progress.query.filter_by(mail=mail)
    db.session.delete(user)
    db.session.delete(progresess)
    db.session.commit()
    return user_schema.jsonify(user)

def login(mail, password):
    user = User.query.filter_by(mail=mail).first()
    if user.password == password:
        return jsonify(message="Correct")
    else:
        return jsonify(message="Incorrect")