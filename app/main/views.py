from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Pitch


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting the categories of pitches
    
    title = 'Home - Welcome to The best  Place to Pitch Website Online'

    interview_pitches = Pitch.get_pitches('interview')
    product_pitches = Pitch.get_pitches('product')
    promotion_pitches = Pitch.get_pitches('promotion')


    
    return render_template('index.html' ,title = title ,interview= interview_pitches,product = product_pitches,promotion = promotion_pitches  )




