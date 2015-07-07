#!/usr/bin/env python3

from flask import Flask, request
app = Flask(__name__)

data = "NA"

@app.route('/')
def main_stats():
	return render_template('main_stats.html', data=data)


@app.route('/post', methods = ['POST'])
def post():
	data = request.json
	print(data)
	return str(data)

if __name__ == '__main__':
	app.run(debug=True)
