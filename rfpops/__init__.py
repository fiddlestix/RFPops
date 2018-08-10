from flask import Flask
from flask import render_template
from flask import redirect
from mongoengine import connect
import webbrowser
from rfpops.forms import AddSingleEntryForm, AddMultipleEntriesForm
from rfpops.database import add_entry

# change this later to use config files or something!
DATABASE_NAME = 'testdb'


def app_factory():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'OMG-CHANGE-THIS-LATER-SERIOUSLY-JUST-FOR-DEVELOPMENT'

    connect(DATABASE_NAME)

    @app.route('/')
    def index():
        from rfpops.database import get_recent_entries
        recent = get_recent_entries()
        return render_template('index.html', recent_entries=recent)

    @app.route('/add', methods=['GET', 'POST'])
    def add():
        form = AddSingleEntryForm()
        if form.validate_on_submit():
            add_entry(form.question.data, form.answer.data, form.name.data)
            return redirect('/')
        return render_template('add.html', form=form)

    @app.route('/batchadd', methods=['GET', 'POST'])
    def batchadd():
        form = AddMultipleEntriesForm()
        return render_template('batchadd.html', form=form)

    @app.route('/explore')
    def explore():
        return render_template('explore.html')

    @app.route('/search')
    def search():
        return render_template('search.html')

    webbrowser.open('http://127.0.0.1:5000/')

    return app
