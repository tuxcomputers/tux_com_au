import os, re
from flask import Blueprint,render_template,redirect,url_for,request

aar_main = Blueprint('main',__name__)

# Home and index
@aar_main.route('/')
@aar_main.route('/index.html')
def index():
    return render_template('aar_index.html')

