# System
import os

# 3rd party
from flask import Flask
from flask.ext.assets import Environment
from flask.ext.compress import Compress
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CsrfProtect

# our code
from assets import app_css, app_js, vendor_css, vendor_js
from config import config
from utils import register_template_utils

basedir = os.path.abspath(os.path.dirname(__file__))

# The following lines do basic instatiation of the mail, database,
# csrf protection, and compression in the application.
# Documentation for Flask-mail: https://pythonhosted.org/flask-mail/
# Documentation for SQLAlchemy: http://www.sqlalchemy.org/
# Documentation for CsrfProtect:
# http://flask-wtf.readthedocs.io/en/latest/csrf.html
#
# Note about CSRF protection. This basically prevents hackers
# from being able to post to our POST routes without having actually
# loaded a form on our website. E.g. they could potentially create
# users if they found out the URL for our register routes and
# the params we expect (its fairly easy to do). But with
# CSRF protection, all forms have a hidden field that is verified on
# our end. This is a bit low level, but there is a SESSION object
# stored on the flask server in memory. Each user has their
# own session containing things like their username, password, etc
# When a form created, a random string called a CSRF token is
# created and is sent along with the form in a hidden field.
# Simultaneously, this string is added to the user session
# stored on the server. When the user submits a form, then
# the server will check to see if the hidden form field with the
# CSRF token matches the CSRF token stored in the user's session
# on the server. If it does, then everything is fine and the
# POST request can proceed normally. If not, then the POST request
# is aborted as a 403 (i think) error is thrown...basically
# the user is not able to POST. This is great for forms, but
# if you want to create a public API that does not require a session,
# then you'll want to include a decorator on your route @csrf.exempt
#
# Compress compresses flask application responses. << NOT SURE WHAT
# THIS ENTAILS.


mail = Mail()
db = SQLAlchemy()
csrf = CsrfProtect()
compress = Compress()

# Set up Flask-Login
# Flask-login provides us with a bunch of easy ways to do secure and
# simple login techniques. LoginManager() is the main class that
# will handle all of this. Session protection makes sure the
# user session is very secure and login_manager.login_view
# Is the view that the a non-authenticated user will get redirected
# to. Otherwise it is a 401 error.


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'

# create_app is called from manage.py with the configuration name
# the config name is then looked up in flask-base/config.py and
# all the config variables are imported.


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Set up extensions
    # init_app(app) are methods in each of these packages

    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    compress.init_app(app)

    # Register Jinja template functions.
    # Notes! Look in ./utils.py. In short this will give us
    # access to some very useful tests and globals in our
    # templates.

    register_template_utils(app)

# Set up asset pipeline
# This one is a bit complex. First an Environment instance is created
# that holds references to a single path to the 'static' folder. We don't
# really care about that since the url_for() method allows us to specify
# access to resources in the static/ directory. But we then append all the
# folders and files within the 'dirs' array to the environment. This
# action provides context for the subsequence set of register actions.
# Looking in app/assets.py there are some Bundle instances created with
# 3 parameters mainly: what type of file(s) to bundle, a type of filter/
# transpiler to apply, and then a final output file. E.g. for the
# app_css bundle, it looks within assets/styles, assets/scripts for any
# *.scss files, converts them to css with the scss transpiler and then
# outputs it to the styles/app.css file. See the templates/partials/_head.html
# file for more information on how to actually include the file.

    assets_env = Environment(app)
    dirs = ['assets/styles', 'assets/scripts']
    for path in dirs:
        assets_env.append_path(os.path.join(basedir, path))
    assets_env.url_expire = True

    assets_env.register('app_css', app_css)
    assets_env.register('app_js', app_js)
    assets_env.register('vendor_css', vendor_css)
    assets_env.register('vendor_js', vendor_js)

    # Configure SSL if platform supports it
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        SSLify(app)

    # Create app blueprints
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from account import account as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix='/account')

    from admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
