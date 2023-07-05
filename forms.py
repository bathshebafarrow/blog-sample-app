from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    user_name = StringField('Enter Your Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
