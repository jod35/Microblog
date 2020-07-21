import os

base_dir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'youcantguessme' 
    SQLALCHEMY_DATABASE_URI=os.path.join(base_dir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False