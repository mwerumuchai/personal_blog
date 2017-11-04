from flask import render_template,redirect,url_for,abort
from . import main
from .. import db

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to '
    return render_template('index.html', title = title)
