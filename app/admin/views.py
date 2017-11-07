from flask import render_template,redirect,url_for,request,flash
from . import admin
from ..models import User,Blog,Comments
from flask_login import login_user,logout_user,login_required,current_user
from .. import db
from .forms import BlogForm

## Admin dashboard
@admin.route('/admin/dashboard')
@login_required
def admin_dashboard():
    '''
    Prevent users from accessing the admin page
    '''
    if not current_user.is_admin:
        abort(403)

    blog = Blog.get_blog()
    return render_template('admin/admin_dashboard.html', title="AdminDashboard",blog=blog)

def check_admin():
    '''
    Prevent non-admins from accessing the page
    '''
    if not current_user.is_admin:
        abort(403)

# blog views
@admin.route('/blogs', methods=['GET','POST'])
@login_required
def list_blogs():
    '''
    List all blogs
    '''
    check_admin()

    blog = Blog.query.all()

    return render_template('admin/post.html',blog=blog, title="Blogs")

@admin.route('/blogs/add', methods=['GET', 'POST'])
@login_required
def add_blog():
    '''
    Blog route function that returns a list of blogs
    '''
    check_admin()

    # if blogs is None:
    #     abort(404)

    add_blog = True

    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data,content=form.content.data)
        try:
            db.session.add(blog)
            db.session.commit()
            flash('Successfully added a new Blog Post.')
        except:
            flash('Error: Blog already exists.')
        return redirect(url_for('.list_blogs'))
    return render_template('admin/posts.html', action = "Add", add_blog=add_blog,form=form,title="Add Department")

# Edit blog
@admin.route('/blogs/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_blog():
    '''
    Route function that edits a blog post
    '''
    check_admin()
    add_blog = False

    blog = Blog.query.get_or_404(id)
    form = BlogForm(obj=blog)
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash('Sussessfully edited the Blog Post')
        return redirect(url_for('admin.list_blogs'))

    form.title.data = blog.title
    form.content.data = blog.content
    return render_template('admin/posts.html', action = 'Edit', add_blog=add_blog,form=form,blog=blog, title="Edit Blog")

# Delete blog
@admin.route('/blogs/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_blog():
    '''
    Route function that deletes a blog post
    '''
    check_admin()

    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    flash('Successfully deleted a blog post')

    return redirect(url_for('admin.list_blogs'))

    return render_template(title="Delete Blog")

# blog views
# @admin.route('/blogs', methods=['GET','POST'])
# @login_required
# def list_blogs():
#     '''
#     List all blogs
#     '''
#     check_admin()
#
#     blog = Blog.query.all()
#
#     return render_template('admin/post.html',blog=blog, title="Blogs")
