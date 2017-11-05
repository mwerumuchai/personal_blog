from flask import render_template,redirect,url_for,abort
from . import main
from .. import db
from ..models import Blog,User,Comments,Role
from flask_login import login_required, current_user
from .forms import BlogForm

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    blog = Blog.get_blog()
    title = 'Home - Welcome to Brownies Blog'
    return render_template('index.html', title = title, blog = blog)

@main.route('/blog/<int:id>')
def blogs(id):
    '''
    Blog route function that returns a list of blogs
    '''

    blog = Blog.query.get(id)

    if blogs is None:
        abort(404)

    title = 'Brownies Blog'
    return render_template('blog.html', title = title, blog = blog)

@main.route('/blog/new/', methods = ['GET','POST'])
def new_blog():
    '''
    New Blog function that returns new blog post
    '''
    form = BlogForm()

    if blogs is None:
        abort(404)

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_blog = Blog(content=content,user_id=current_user.id, title=title)
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'New Blog'
    return render_template('new_blog.html', title = title, blog_form = form)
