from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Algorithm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    pseudocode = db.Column(db.Text)
    implementation = db.Column(db.Text)
    complexity = db.Column(db.String(100))
    usage = db.Column(db.Text)
