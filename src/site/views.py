from . import app
from flask import render_template, request

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

@app.route('/query')
def query():
	query = request.args.get('i')
	processed_query = 'Processed query goes here'
	result = 'Result goes here'
	declarations = []
	for key in request.args:
		if key == 'i':
			continue
		declarations.append({'name': key, 'input': request.args.get(key)})
	return render_template('query.html', 
		query=query,
		processed_query=processed_query,
		result=result,
		declarations=declarations
	)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html', error=error), 404