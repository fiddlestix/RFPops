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
        return render_template('index.html')

    webbrowser.open('http://127.0.0.1:5000/')

    # testing the search function... delete later!
    import rfpops.model
    print(model.search_entries("quest"))

    return app
