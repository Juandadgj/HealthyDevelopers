from ..config.database.database import db, mar

class Habit(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(45), nullable=False)

    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category

class HabitSchema(mar.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'category')

habit_schema = HabitSchema()
habits_schema = HabitSchema(many=True)
