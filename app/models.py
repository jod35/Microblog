from app import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),nullable=False)
    passwd_hash=db.Column(db.String(128))


    def __init__(self,username,passwd_hash):
        self.username=username
        self.passwd_hash=passwd_hash

    def __repr__(self):
        return f"{self.username}'s Account"