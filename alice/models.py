from django.db.models import *


# Create your models here.

class Person(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=32)
    sex = IntegerField()
    address = CharField(max_length=100)


class Hobbit(Model):
    id = AutoField(primary_key=True)
    who = ForeignKey(Person, on_delete=CASCADE)
    hobbit_name = CharField(max_length=32)


class Job(Model):
    id = AutoField(primary_key=True)
    jobName = CharField(max_length=32)


class PersonAndJob(Model):
    id = AutoField(primary_key=True)
    person = ForeignKey(Person, on_delete=CASCADE)
    job = ForeignKey(Job, on_delete=CASCADE)
    salary = IntegerField(default=0)
