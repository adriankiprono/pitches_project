from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    category = SelectField('Type',choices=[('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch')],validators=[Required()])
    submit = SubmitField('Submit')