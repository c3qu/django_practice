from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer

from alice.models import Navigation


class NavigationSerializerForSuperUser(ModelSerializer):
    permission = IntegerField(read_only=True, source="permission.id")

    class Meta:
        model = Navigation
        fields = '__all__'


class NavigationSerializer(ModelSerializer):
    category = CharField(max_length=64, read_only=True)
    permission = IntegerField(read_only=True, source="permission.id")

    class Meta:
        model = Navigation
        fields = '__all__'
