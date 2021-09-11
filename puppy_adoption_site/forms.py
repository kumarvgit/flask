from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add puppy')


class DelForm(FlaskForm):
    id = IntegerField('ID of puppy to remove')
    submit = SubmitField('Remove Puppy')


class AddOwner(FlaskForm):
    name = StringField('What is your name')
    pup_id = IntegerField('Id of puppy')
    submit = SubmitField('Add Owner')
