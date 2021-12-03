import os, re
from flask import Blueprint,render_template,redirect,url_for,request

tux_main = Blueprint('main',__name__)

# Home and index
@tux_main.route('/')
@tux_main.route('/index.html')
def index():
    return render_template('tux_index.html')

@tux_main.route('/skills')
def skills():
    return render_template('tux_skills.html')

@tux_main.route('/portfolio')
def portfolio():
    return render_template('tux_portfolio.html')

@tux_main.route('/experience')
def experience():
    return render_template('tux_experience.html')

@tux_main.route('/contact')
def contact():
    return render_template('tux_contact.html')

