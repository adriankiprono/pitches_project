from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch Nmae',validators=[Required()])
    
    category = SelectField('Type',choices=[('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch')],validators=[Required()])
    text = TextAreaField('Description', validators=[Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    text = TextAreaField('comment on this pitch',validators=[Required()])
    submit = SubmitField('Submit')