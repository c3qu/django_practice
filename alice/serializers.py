from rest_framework.serializers import ModelSerializer

from alice.models import Person, Hobbit, Job, PersonAndJob


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class HobbitSerializer(ModelSerializer):
    class Meta:
        model = Hobbit
        fields = '__all__'


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class PersonAndJobSerializer(ModelSerializer):
    class Meta:
        model = PersonAndJob
        fields = '__all__'
