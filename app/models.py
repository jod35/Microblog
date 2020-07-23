from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),nullable=False,unique=True)
    bio=db.Column(db.String(140))
    last_seen=db.Column(db.DateTime(),default=datetime.utcnow)
    passwd_hash=db.Column(db.String(128),nullable=False)
    email=db.Column(db.String(40),nullable=False,unique=True)
    posts=db.relationship('Post',backref='author',lazy=True)
    


    # def __init__(self,username,email,passwd_hash):
    #     self.username=username
    #     self.email=email
    #     self.passwd_hash=passwd_hash

    def __repr__(self):
        return f"{self.username}'s Account"

    def set_password(self,password):
        self.passwd_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.passwd_hash,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(40),nullable=False)
    body=db.Column(db.Text(),nullable=False)
    created=db.Column(db.DateTime(),default=datetime.utcnow,index=True)

    user_id=db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __init__(self,title,body,created):
        self.title=title
        self.body=body
        self.created=created

    def __repr__(self):
        return f"<Post {self.title}>"