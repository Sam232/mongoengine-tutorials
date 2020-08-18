from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class Post(Document):
    title = StringField(unique=True, required=True)
    description = StringField(required=True, max_length=150)
    status = StringField(choices=["ACTIVE", "INACTIVE"])
    date_created = DateTimeField(default=datetime.utcnow())
    date_updated = DateTimeField()
