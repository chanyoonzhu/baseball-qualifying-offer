import json
from data_analysis.main import *
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")

def hello():
    try:
        return render_template('index.html')
    except Exception as e:
	    render_template("500.html", error = str(e))

@app.route("/fetch")

def fetch():
    try:
        data = fetch_data()
        callback = request.args.get('callback')
        return '{0}({1})'.format(callback, data)
    except Exception as e:
        render_template("500.html", error = str(e))

@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run()