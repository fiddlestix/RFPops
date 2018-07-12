from flask import Flask
from flask import render_template
from mongoengine import connect
import webbrowser

# change this later to use config files or something!
DATABASE_NAME = 'testdb'


def app_factory():
    app = Flask(__name__)

    connect(DATABASE_NAME)

    @app.route('/')
    def index():
        from rfpops.database import get_recent_entries
        recent = get_recent_entries()
        return render_template('index.html', recent_entries=recent)

    @app.route('/add')
    def add():
        return render_template('add.html')

    @app.route('/explore')
    def explore():
        return render_template('explore.html')

    @app.route('/search')
    def search():
        return render_template('search.html')

    webbrowser.open('http://127.0.0.1:5000/')

    return app
