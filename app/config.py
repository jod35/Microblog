import os

base_dir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'youcantguessme' 
    # SQLALCHEMY_DATABASE_URI='sqlite://'+ os.path.join(base_dir,'app.db')
    

    #for windows, I am on windows
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///C:/Users/Jonathan/coding/migroblog/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False