from rest_framework.serializers import ModelSerializer

from alice.models import Person, Hobbit


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class HobbitSerializer(ModelSerializer):
    class Meta:
        model = Hobbit
        fields = '__all__'
