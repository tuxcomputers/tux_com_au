import os, re
from flask import Blueprint,render_template,redirect,url_for,request

tux_main = Blueprint('main',__name__)

# Home and index
@tux_main.route('/')
@tux_main.route('/index.html')
def index():
    return render_template('hac_index.html')

