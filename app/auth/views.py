from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .forms import RegistrationForm
from .. import db



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,firstname= form.firstname.data,lastname= form.lastname.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to One Minute Pitch","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)