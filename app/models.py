from app import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),nullable=False)
    passwd_hash=db.Column(db.String(128))
    email=db.Column(db.String(40),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)
    


    def __init__(self,username,passwd_hash):
        self.username=username
        self.passwd_hash=passwd_hash

    def __repr__(self):
        return f"{self.username}'s Account"


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