from . import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/playground')
def playground():
	return render_template('playground.html')

@app.route('/help')
def help():
	return render_template('help.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html', error=error), 404