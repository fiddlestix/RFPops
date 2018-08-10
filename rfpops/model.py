from mongoengine import Document
from mongoengine import StringField
from mongoengine import DateTimeField


class Entry(Document):
    question = StringField(required=True)
    answer = StringField(required=True)
    customer_name = StringField(required=True)
    date_added = DateTimeField(required=True)

    meta = {
        'indexes': [
            {'fields': ['$question', '$answer', '$customer_name'],
             'default_language': 'english',
             'weights': {'question': 10, 'answer': 9, 'name': 8}}],
    }


