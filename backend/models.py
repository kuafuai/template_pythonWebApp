# Import necessary modules and libraries
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance
db = SQLAlchemy()

# Define database models using SQLAlchemy ORM
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Define other device attributes

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Define other location attributes

# Define relationships between models if necessary
# No relationships defined in the original code, so no modifications needed.