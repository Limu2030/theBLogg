from flask import Flask
from app import create_app,db
from flask_script import Manager,Server
from app import models
from  flask_migrate import Migrate, MigrateCommand

from app.models import User

