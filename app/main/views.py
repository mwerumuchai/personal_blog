from flask import render_template,redirect,url_for,abort
from . import main
from .. import db
from ..models import Blog,User,Comments
from flask_login import login_required, current_user
from .forms import BlogForm, CommentForm
import markdown2

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    blog = Blog.get_blog()
    title = 'Home - Welcome to Brownies Blog'
    return render_template('index.html', title = title, blog = blog)

# #homepage
# @main.route('/blog/<int:id>')
# def blogs(id):
#     '''
#     Blog route function that returns a list of blogs
#     '''
#
#     blog = Blog.query.get(id)
#
#     if blogs is None:
#         abort(404)
#
#     comment_id = Comments.get_comments(id)
#     title = f'Blog {blog.id}'
#     return render_template('homepage.html', title = title, blog = blog, comment_id = comment_id)
#

@main.route('/blog/<int:id>')
def blogs(id):
    '''
    Blog route function that returns a list of blogs
    '''

    blog = Blog.query.get(id)

    if blogs is None:
        abort(404)

    comment_id = Comments.get_comments(id)
    title = f'Blog {blog.id}'
    return render_template('blog.html', title = title, blog = blog, comment_id = comment_id)

# single blog
@main.route('/blog/<int:id>')
def single_blog(id):
    '''
    Function that handles viewing a single review
    '''
    blog=Blog.query.get(id)

    if blogs is None:
        abort(404)

    format_blog = markdown2.markdown(blog.content,extras=["code-friendly", "fenced-code-blocks"])

    return render_template('blogger_post.html', title = title, blog = blog, content = content, format_blog = format_blog)
# comment on blogs
@main.route('/blog/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    '''
    New comment function that returns a form to create a comment on a new page
    '''
    blog = Blog.query.filter_by(id=id).first()

    if blogs is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        comment_section = form.comment_section.data
        new_comment = Comments(comment_section=comment_section, blog_id=blog.id, user=current_user)
        new_comment.save_comment()

        return redirect(url_for('.blogs', id = blog.id))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)

# switch to blogger page
@main.route('/blogger')
@login_required
def blogger():
    '''
    Blogger function that returns the  blogger's page and all its data
    '''
    title = 'Blogger'
    blog = Blog.get_blog()

    return render_template('blogger.html', title=title, blog=blog)


@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
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

    title = 'Create New Blog'
    return render_template('new_blog.html', title = title, blog_form = form)
