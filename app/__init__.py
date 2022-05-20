from flask import Flask
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy

from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(config_options[config_name])

bootstrap.init_app(app)
db.init_app(app)
