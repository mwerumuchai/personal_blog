from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    '''
    Blog class define Blog
    '''
    __tablename__ = 'blog'

    # add columns
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.now)

    # save
    def save_blog(self):
        '''
        Function that saves Blog
        '''

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls):
        '''
        Function that returns all the data from blog after being queried
        '''
        blog = Blog.query.all()
        return blog
