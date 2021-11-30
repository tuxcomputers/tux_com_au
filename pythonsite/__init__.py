# napp.py
from flask import Flask, render_template

# Create the flask App
def create_app():
    napp=Flask(__name__)
    napp.debug=True

    # Main views - public has access to
    from .aar_views_main import aar_main
    napp.register_blueprint(aar_main)

    return napp
