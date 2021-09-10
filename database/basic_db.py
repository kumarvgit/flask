import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# name of actual file of python here basic_db.py
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Setup the console database from the application
# set the env var as export FLASK_APP=basic_db.py else console wont work
# create migration directory flask db init
# flask db migrate -m 'Created Puppy table'
# flask db upgrade
Migrate(app, db)

# Models - Begin


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year(s) old and breed is {self.breed}"

# Models - END


if __name__ == '__main__':
    print(f'SQLIte db in use at base dir{basedir}')
    app.run(debug=True)
