from ..config.database.database import db, mar

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

class UserSchema(mar.Schema):
    class Meta:
        fields = ('id', 'name', 'last_name', 'sex', 'mail', 'password', 'phone', 'direction')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
