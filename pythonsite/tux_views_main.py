import os, re
from flask import Blueprint,render_template,redirect,url_for,request
import datetime

tux_main = Blueprint('main',__name__)

def file_dtm (file_name): # Take a template file name and return the date it was last modified
    directory_path = os.getcwd()
    filename = directory_path + '/pythonsite/templates/' + file_name
    file_details = os.path.getmtime(filename)
    file_dtm = datetime.datetime.fromtimestamp(file_details)
    date_string = file_dtm.strftime("%d %B %Y")
    return date_string

# Home and index
@tux_main.route('/')
@tux_main.route('/index.html')
def index():
    file = 'tux_index.html'
    file_date = file_dtm(file)
    return render_template(file, dtm=file_date)

@tux_main.route('/skills')
def skills():
    file = 'tux_skills.html'
    file_date = file_dtm(file)
    return render_template(file, dtm=file_date)

@tux_main.route('/portfolio')
def portfolio():
    file = 'tux_portfolio.html'
    file_date = file_dtm(file)
    return render_template(file, dtm=file_date)

@tux_main.route('/experience')
def experience():
    file = 'tux_experience.html'
    file_date = file_dtm(file)
    return render_template(file, dtm=file_date)

@tux_main.route('/contact')
def contact():
    file = 'tux_contact.html'
    file_date = file_dtm(file)
    return render_template(file, dtm=file_date)

