from mongoengine import Document
from mongoengine import StringField
from mongoengine import DateTimeField
import csv
from collections import namedtuple


from datetime import datetime


class Entry(Document):
    question = StringField(required=True)
    answer = StringField(required=True)
    customer_name = StringField(required=True)
    date_added = DateTimeField(required=True)

    meta = {'indexes': [
        {'fields': ['$question', '$answer', '$customer_name'],
         'default_language': 'english',
         'weights': {'question': 10, 'answer': 9, 'name': 8}}
    ]}


def add_entry(quest, ans, name):
    entry = Entry(question=quest, answer=ans, customer_name=name, date_added=datetime.now())
    entry.save()


def add_from_csv(filename):
    with open(filename, 'rt') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entry = Entry(row['question'], row['answer'], row['customer_name'], row['date_added'])
            entry.save()


def search_entries(string):
    results = Entry.objects.search_text(string).order_by('$text_score')
    return results
