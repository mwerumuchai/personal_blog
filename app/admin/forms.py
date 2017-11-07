from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class BlogForm(FlaskForm):
    '''
    RegistrationForm class that passes in the required and email validators
    '''
    title = StringField('Title')
    content = TextAreaField('New Blog')
    submit = SubmitField('Submit')


#     #custom validators
#     def validate_email(self,data_field):
#         '''
#         Functions takes in the data field and checks our database to confirm user Validation
#         '''
#         if User.query.filter_by(email = data_field.data).first():
#             raise ValidationError('there is an account with that email')
#
#     def validate_username(self,data_field):
#         '''
#         Function checks if the username is unique and raises ValidationError
#         '''
#         if User.query.filter_by(username = data_field.data).first():
#             raise ValidationError('that user name is taken')
#
# # LOgin form that has 3 fields
# class LoginForm(FlaskForm):
#     email=StringField('your email address',validators=[Required(),Email()])
#     password=PasswordField('password',validators=[Required()])
#     remember = BooleanField('remember me')
#     submit=SubmitField('sign in')
