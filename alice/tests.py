# Create your tests here.
from django.db.models import Sum, When, Case
from alice.models import PersonAndJob, Person


# python .\manage.py shell -c "from alice import tests;tests.test_group_by()"
def test_group_by():
    """Animals that can speak are correctly identified"""
    person_and_job = PersonAndJob.objects.values("person").annotate(
        cnt=Sum(Case(
            When(salary=0, then=0),
            default=1
        ))).filter(cnt=0)
    print(person_and_job)


def test_no():
    cc=Person.objects.filter(personandjob=None)
    print(cc)
