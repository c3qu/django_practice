# Create your tests here.
from django.db.models import Sum, When, Case
from django.test import TestCase

from alice.models import PersonAndJob


def test_group_by():
    """Animals that can speak are correctly identified"""
    person_and_job = PersonAndJob.objects.values("person").annotate(
        cnt=Sum(Case(When(salary=0, then=0), default=1))).filter(cnt=0)

    print(person_and_job)
