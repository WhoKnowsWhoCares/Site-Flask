from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp

class SubmitForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    message = StringField('Message', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Submit')


