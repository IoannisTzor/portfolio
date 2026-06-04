from extensions import db
from datetime import datetime

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    contributors = db.Column(db.String(200), nullable=True)
    technologies = db.Column(db.String(200), nullable=False)
    github_url = db.Column(db.String(200))
    live_url = db.Column(db.String(200))

    def __repr__(self):
        return f'<Project {self.title}>'
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    message = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    