import subprocess, time
from flask import Blueprint, jsonify, request

playground = Blueprint('playground', __name__, url_prefix='/playground')

@playground.route('/run', methods=['POST'])
def run():
	fname = 'bin/playground/' + str(round(time.time() * 1000))

	with open(fname + '.cc', 'w+') as f:
		f.write('''#include <iostream> int main(int argc, char *argv[]) {''')
		f.write(request.json['code'])
		f.write('''return 0;}''')

	build_output = '' 
	run_output = ''
	response = {
		'build_output': build_output,
		'run_output': run_output
	}
	return jsonify(response), 200