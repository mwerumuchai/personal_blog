from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class BlogForm(FlaskForm):
    title = TextAreaField('Title')
    content = TextAreaField('New Blog')
    submit = SubmitField('Submit')
