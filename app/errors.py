from app import app,db
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(error):
    db.session.rollback()
    return render_template('500,html')

