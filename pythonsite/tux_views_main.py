import os, re
from flask import Blueprint,render_template,redirect,url_for,request
import datetime

tux_main = Blueprint('main',__name__)

def file_dtm (file_name):
    file_dtm = ''
    directory_path = os.getcwd()
    filename = directory_path + '/pythonsite/templates/' + file_name
    file_dtm = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    file_string = file_dtm.strftime("%a %d %B %Y")
    return file_string
    

# Home and index
@tux_main.route('/')
@tux_main.route('/index.html')
def index():
    file = 'tux_index.html'
    file_time = file_dtm(file)
    return render_template(file, dtm=file_time)

@tux_main.route('/skills')
def skills():
    file = 'tux_skills.html'
    file_time = file_dtm(file)
    return render_template(file, dtm=file_time)

@tux_main.route('/portfolio')
def portfolio():
    file = 'tux_portfolio.html'
    file_time = file_dtm(file)
    return render_template(file, dtm=file_time)

@tux_main.route('/experience')
def experience():
    file = 'tux_experience.html'
    file_time = file_dtm(file)
    return render_template(file, dtm=file_time)

@tux_main.route('/contact')
def contact():
    file = 'tux_contact.html'
    file_time = file_dtm(file)
    return render_template(file, dtm=file_time)

