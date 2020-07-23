from app import app,db
from flask import render_template,flash,request,redirect,url_for
from .forms import LoginForm,RegistrationForm,EditProfileForm
from flask_login import current_user,login_user,logout_user,login_required
from .models import User,Post
from werkzeug.urls import url_parse
from datetime import datetime

posts=[
    {
        'id':1,
        'author':"Sjonathan",
        "content":"What a good day"
    },
    {
        'id':2,
        'author':'Json',
        "content":"Hey There my gorgeous friends"
    }
]

@app.route('/')
@app.route('/index')
def index():
    user={
        'user':"Jonathan"
    }



    title="Hello"
    return render_template('index.html',title=title,posts=posts)
           

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))


    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()

        if not user and not user.check_password(user.passwd_hash,form.password.data):
            flash("Invalid username or password!")

            return redirect(url_for('login'))

        login_user(user,remember=form.remember_me.data)

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':

            next_page=url_for('index')
        return redirect(next_page)

    return render_template('login.html',form=form,title="Login")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile/<username>')
@login_required
def user_profile(username):
    user=User.query.filter_by(username=username).first()


    return render_template('profile.html',user=user)


@app.route('/register',methods=['GET','POST'])
def sign_up():
    form=RegistrationForm()
    if request.method =='POST':
        new_user=User(username=request.form.get('username'),email=request.form.get('email'))
        new_user.set_password(request.form.get('password'))

        db.session.add(new_user)
        db.session.commit()

        flash("Account Created successfully, You can now log in.")

        return redirect(url_for('login'))

    return render_template('signup.html',form=form)


#record last visit
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen=datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile/',methods=['GET','POST'])
def edit_profile():

    form=EditProfileForm()

    if request.method == "POST":
        current_user.username=request.form.get('username')
        current_user.bio=request.form.get('bio')
        db.session.commit()

        flash("Changes updated successfully")
        return redirect(url_for('user_profile',username=current_user.username))

    elif request.method == "GET":
        form.username.data=current_user.username
        form.bio.data=current_user.bio
    return render_template('editprofile.html',form=form)







