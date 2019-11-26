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

@main.route('/pitch/new', methods = ['GET','POST'])
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html',title = title,pitch_form=pitch_form )




