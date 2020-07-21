from app import app
from flask import render_template,flash,request,redirect
from .forms import LoginForm


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
@app.route('/hello')
def hello():
    user={
        'user':"Jonathan"
    }



    title="Hello"
    return render_template('index.html',user=user,title=title,posts=posts)
           

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {} , remember_me ={}".format(form.username.data,form.remember_me.data))
        return redirect('/')
    return render_template('login.html',form=form,title="Login")