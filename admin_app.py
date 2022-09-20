
import logging
# import os
# import traceback

from flask import  Flask
from flask_cors import CORS
from time import time 
from db_home.models import db


__author__ = 'Tahir'

app = Flask(__name__)

logging.basicConfig(level=logging.INFO,
                    format="%(threadName)s %(asctime)s %(name)-12s %(message)s",
                    datefmt="%d-%m-%y %H:%M")

app.config.from_object('configuration')

CORS(app, headers=['Content-Type', 'Authorization'])

db.init_app(app)

with app.app_context():
    db.create_all()
                                                                  