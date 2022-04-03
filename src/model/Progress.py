from ..config.database.database import db, mar

class Progress(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    usermail = db.Column(db.String(255), nullable=False)
    habitid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, usermail, habitid, status):
        self.usermail = usermail
        self.habitid = habitid
        self.status = status

class ProgressSchema(mar.Schema):
    class Meta:
        fields = ('id', 'usermail', 'habitid', 'status')


progress_schema = ProgressSchema()
progresess_schema = ProgressSchema(many=True)
