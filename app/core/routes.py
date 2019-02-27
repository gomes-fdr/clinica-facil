from flask import render_template
from app.core import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')