# app/models.py

from app import db

class Project(db.Model):
    __tablename__ = 'projects'  # Name of the table

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Project {self.name}>"
