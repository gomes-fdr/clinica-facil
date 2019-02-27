from flask import render_template
from app.core import bp

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')