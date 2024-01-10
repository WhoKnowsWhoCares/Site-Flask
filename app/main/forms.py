from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class MessageForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(1, 64)])
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    message = StringField('message', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('submit')


