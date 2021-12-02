# napp.py
from flask import Flask, render_template

# Create the flask App
def create_app():
    napp=Flask(__name__)
    napp.debug=True

    # Main views - public has access to
    from .tux_views_main import tux_main
    napp.register_blueprint(tux_main)

    return napp
