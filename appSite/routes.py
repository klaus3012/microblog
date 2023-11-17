from appSite import appSite
from flask import render_template

@appSite.route('/')
@appSite.route('/index')
def index():
    nome = 'World'
    return render_template('index.html')