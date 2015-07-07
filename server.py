#!/usr/bin/env python3
import json
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

data = "NA"

@app.route('/')
def main_stats():
	f = open('data.json')
	for line in f:
		json_data = line

	data = json.loads(json_data)
	
	return render_template('main_stats.html', data=data)


@app.route('/post', methods = ['POST'])
def post():
	json_data = request.json
	f = open('data.json', 'a')
	f.write('\n')
	json.dump(json_data, f)
	return str(json_data)

if __name__ == '__main__':
	app.run(debug=True)
