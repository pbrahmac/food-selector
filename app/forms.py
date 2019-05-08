from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class MealtimeForm(FlaskForm):
    mealtime = SelectField(u'Choose Mealtime', validators=[DataRequired()], choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')])
    submit = SubmitField('Go')