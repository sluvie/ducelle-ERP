import logging

TIMEZONE = 'Asia/Jakarta'

APP_NAME = "ducelle-System"

# DEBUG can only be set to True in a development environment for security reasons
DEBUG = True

# user session dummy
USER_DUMMY = {
    "accountname": "Sulianto Suhono",
    "accountemail": "sulianto.suhono@gmail.com"
}

# secret key for generating tokens
SECRET_KEY = "ducelle-system-2023"
AES_KEY = "ducelle-system-2023"

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'Pa$$word1')

# Configuration of a Email account for sending and receiving mails
MAIL_ACCOUNT = [
    {
        "default": {
            "ACCOUNT": "rocket.saas@gmail.com",
            "SERVER": "smtp.googlemail.com",
            "IMAP_PORT": 993,
            "SMTP_PORT": 465,
            "USE_TLS": False,
            "USE_SSL": True,
            "USERNAME": "",
            "PASSWORD": ""
        }
    }
]

# Configuration of a Database account
DATABASE_ACCOUNT = {
        "ducellesystem_db": {
            "server": "51.79.206.3",
            "port": 5499,
            "user": "ducellesystem",
            "password": "iamducellesystem",
            "database": "ducellesystem_db",
        },
    }

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

LOG_LEVEL = logging.DEBUG
LOG_FILENAME = 'activity.log'
LOG_MAXBYTES = 1024
LOG_BACKUPS = 2

# Application
APP_TITLE = "ducelle-ERP"
APP_VERSION = "1.0.0"