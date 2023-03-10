from flask import (
        render_template, 
        g,
        request,
        session,
        redirect,
        url_for,
        flash
)
from app import app
from app import config

# database
from app.models.user import User_m

# libraries
from app.libraries.cipher import AESCipher


@app.route('/login', methods = ['GET', 'POST'])
def login():
        if request.method == "POST":
                account = {
                        "email": request.form.get('email'),
                        "password": request.form.get('password')
                }
                
                user_m = User_m()
                validate = user_m.validate_login(account)
                if validate:
                        user, message = user_m.get(account)
                        session['user'] = user
                        return redirect(url_for('index'))
                else:
                        flash('User invalid.')
                
        return render_template('pages/login.html', title=config.APP_TITLE)


@app.route('/signup', methods = ['POST'])
def signup():
        try:
                account = {
                        'name': request.form.get('accountname'),
                        'username': request.form.get('accountusername'),
                        'email': request.form.get('accountemail'),
                        'password': request.form.get('accountpassword'),
                        'secretkey': '',
                        'createby': 'system-signup'
                }
<<<<<<< HEAD
=======

>>>>>>> 053f8f19361fc7014fcc177203a0c9920887ffb2
                user_m = User_m()
                
                # validate the email
                # if already exist show the message
                validate = user_m.validate_register(account['email'])
                if validate:
                        flash('User already exist.')
                        return render_template('pages/login.html', title=config.APP_TITLE)
                else:
                        try:
                                cipher = AESCipher(config.AES_KEY)
                                secretkey = cipher.encrypt(account['email'])
                                account['secretkey'] = secretkey
                                user_m.insert([account])
                        except Exception as e:
                                flash(str(e))
                                return render_template('pages/login.html', title=config.APP_TITLE)
        except Exception as e:
                flash(str(e))
                
        return render_template('pages/login.html', title=config.APP_TITLE)


@app.route('/logout', methods = ['GET'])
def logout():
        session.pop('user', None)
        g.user = None
        return render_template('pages/login.html', title=config.APP_TITLE)