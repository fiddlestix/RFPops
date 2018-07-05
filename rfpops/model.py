from mongoengine import Document
from mongoengine import StringField
from mongoengine import DateTimeField
from mongoengine import connect
from datetime import datetime

# change this later to use config files or something!
DATABASE_NAME = 'testdb'


class Entry(Document):
    question = StringField(required=True)
    answer = StringField(required=True)
    customer_name = StringField(required=True)
    date_added = DateTimeField(required=True)


def add_entry(quest, ans, name):
    connect(DATABASE_NAME)
    entry = Entry(question=quest, answer=ans, customer_name=name, date_added=datetime.now())
    entry.save()
