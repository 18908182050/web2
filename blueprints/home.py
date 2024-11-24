from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@home_bp.route('/')
def home():
    return render_template('home.html')

@home_bp.route('/error')
def error():
    return render_template('error.html')
