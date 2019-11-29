from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch
from .forms import PitchForm,UpdateProfile
import datetime
from flask_login import login_required,current_user
from .. import db,photos


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

@main.route('/user/<uname>')
def profile(uname):
    user_id = current_user.id
    user = User.query.filter_by(username = uname).first()
    
    user_joined = user.date_joined.strftime('%b %d, %Y')
    pitches = Pitch.query.filter_by(user_id=user.id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,  date= user_joined, pitches=pitches)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods= ['GET','POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    user=current_user.id
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        category = pitch_form.category.data
        pitch = pitch_form.text.data

        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,likes=0,dislikes=0,user_id=user)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html',title = title,pitch_form=pitch_form )

@main.route('/pitches/interview_pitches')
def interview_pitches():

    pitches = Pitch.get_pitches('interview')

    return render_template("interview_pitches.html", pitches = pitches)

@main.route('/pitches/product_pitches')
def product_pitches():

    pitches = Pitch.get_pitches('product')

    return render_template("product_pitches.html", pitches = pitches)

@main.route('/pitches/promotion_pitches')
def promotion_pitches():

    pitches = Pitch.get_pitches('promotion')

    return render_template("promotion_pitches.html", pitches = pitches)
@main.route('/pitch/<int:id>', methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.posted.strftime('%b %d, %Y')
    
    

    if request.args.get("like"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    


    return render_template("pitch.html", pitch = pitch)


@main.route('/user/<uname>/pitches')
def user_pitches(uname):
    user=current_user.id
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    
    
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/pitches.html", user=user,pitches=pitches,date = user_joined,user_id=user)
    

    
 





