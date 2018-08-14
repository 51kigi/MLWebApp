#flask_blog/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

appa=Flask(__name__)
appa.config.from_object('flask_blog.config')

db=SQLAlchemy(appa)
import flask_blog.views