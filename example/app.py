from flask import Flask, render_template, abort, current_app
from flask_sentry import Sentry


app = Flask(__name__)
Sentry(app)


@app.route("/")
def index():
    try:
        raise Exception("An error occurred")
    except Exception as e:
        current_app.logger.error(e)
    return render_template("index.html")
 