from flask import Flask ## import Flask dari package flask

app = Flask(__name__)

# setup the app with config.py file
app.config.from_object('app.config')

# setup the logger
from app.logger_setup import logger

# set secret key
app.secret_key = app.config['SECRET_KEY']

# config file upload
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024

# import the controllers
from app.controllers import  *

# TODO: add your blueprint page in here
app.register_blueprint(system.systembp)