from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
  return "<h1>HELLO</h1>"

@views.route('/info')
def info():
  return "<h1>INFO</h1>"