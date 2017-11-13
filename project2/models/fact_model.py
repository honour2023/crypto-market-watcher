from models.base_model import *
from peewee import CharField, BooleanField, TextField, DateTimeField

from datetime import datetime

class FactModel(BaseModel):
    user = CharField(40)
    fact = TextField(20)
    is_true = BooleanField()
    timestamp = DateTimeField(default=datetime.now)

class Message(BaseModel):
	name = CharField(50)
	email = CharField(30)
	message = CharField(40)
	title=CharField(20)
