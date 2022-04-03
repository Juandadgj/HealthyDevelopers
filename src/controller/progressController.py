from flask import request, jsonify
from ..config.database.database import db
from ..model.Progress import Progress, progress_schema, progresess_schema


def getProgress(mail):
    progress = Progress.query.filter_by(usermail=mail)
    result = progresess_schema.dump(progress)
    return jsonify(result)

def createProgress():
    usermail = request.json['usermail']
    habitid = request.json['habitid']
    status = request.json['status']

    new_progress = Progress(usermail, habitid, status)
    db.session.add(new_progress)
    db.session.commit()
    return progress_schema.jsonify(new_progress)

def updateProgress():
    mail = request.json['usermail']
    habitid = request.json['habitid']
    progress = Progress.query.filter_by(usermail=mail, habitid=habitid).first()
    status = request.json['status']
    progress.status = status
    db.session.commit()
    return progress_schema.jsonify(progress)

def deleteProgress(mail):
    mail = mail
    progress = Progress.query.filter_by(usermail=mail).order_by(Progress.id.desc()).first()
    db.session.delete(progress)
    db.session.commit()
    return progress_schema.jsonify(progress)
