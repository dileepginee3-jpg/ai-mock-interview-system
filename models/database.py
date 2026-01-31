from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False) # 'Technical' or 'HR'
    reference_answer = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Question {self.text[:20]}...>'

class InterviewSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, default=0.0)
    date_taken = db.Column(db.DateTime, default=datetime.utcnow)
    details = db.Column(db.Text, nullable=True) # JSON string or detailed text of Q&A

    def __repr__(self):
        return f'<Session {self.user_name} - {self.score}>'
