from app import app
from flask import render_template

@app.route('/')
@app.route('/hello')
def hello():
    user={
        'user':"Jonathan"
    }

    title="Hello"
    return render_template('index.html',user=user,title=title)
           