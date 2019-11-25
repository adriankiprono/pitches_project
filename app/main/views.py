from flask import render_template,request,redirect,url_for
from . import main


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    
    title = 'Home - Welcome to The best  Place to Pitch Website Online'

    
    return render_template('index.html' )




