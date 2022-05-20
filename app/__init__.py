from flask import Flask
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy

from config import config_options


app = Flask(__name__)