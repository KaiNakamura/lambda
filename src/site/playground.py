import subprocess, time
from flask import Blueprint, jsonify, request

playground = Blueprint('playground', __name__, url_prefix='/playground')

@playground.route('/run', methods=['POST'])
def run():
	fname = 'bin/playground/' + str(round(time.time() * 1000))

	with open(fname + '.cc', 'w+') as f:
		f.write('''#include <iostream>\nint main(int argc, char *argv[]) {''')
		f.write(request.json['code'])
		f.write('''return 0;}''')

	build_command = 'g++ {0}.cc -o {0}.a; exit 0'.format(fname)
	build_output = subprocess.check_output(
		build_command, 
		stderr=subprocess.STDOUT, 
		shell=True
	).decode("utf-8")

	run_command = './{0}.a; exit 0'.format(fname)
	run_output = subprocess.check_output(
		run_command,
		stderr=subprocess.STDOUT,
		shell=True
	).decode("utf-8")

	response = {
		'build_output': build_output,
		'run_output': run_output
	}
	return jsonify(response), 200