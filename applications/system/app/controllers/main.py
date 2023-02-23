from flask import (
    render_template, 
    g,
    request,
    session,
    redirect,
    url_for
)
from app import app
from app import config

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        # find user based on userid, update information user
        user = session['user']
        g.user = user


@app.route('/', methods = ['GET'])
@app.route("/index")
def index():
    if not g.user:
        return redirect(url_for('login'))
    
    user = g.user      
    return render_template('index.html', title=config.APP_TITLE)