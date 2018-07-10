from datetime import datetime
import csv
from rfpops.model import Entry


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
    from mongoengine import QuerySet
    results = QuerySet.search_text(Entry.objects, string)
    return results
