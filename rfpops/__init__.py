from flask import Flask
from flask import render_template


def app_factory():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
