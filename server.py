from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_stats():
	    return render_template('main_stats.html', )


if __name__ == '__main__':
	app.run(debug=True)
