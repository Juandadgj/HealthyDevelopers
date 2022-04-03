from flask import request, jsonify
from ..config.database.database import db
from ..model.Habit import Habit, habit_schema, habits_schema

def getHabits():
    all_habits = Habit.query.all()
    result = habits_schema.dump(all_habits)
    return jsonify(result)
