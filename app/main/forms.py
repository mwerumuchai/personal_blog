from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class BlogForm(FlaskForm):
    title = TextAreaField('Title')
    content = TextAreaField('New Blog')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_section = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
