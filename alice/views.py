from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from alice.models import Person, Hobbit
from alice.serializers import PersonSerializer, HobbitSerializer
from hi.settings import STATICFILES_DIRS


# Create your views here.
class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=False, methods=['post', 'get'])
    def get_person_by_hobbit(self, request):
        hobbit_name_list = request.data.get("hobbit_name_list")
        print(request.data)
        result_persons = Person.objects.filter(hobbit__hobbit_name__in=hobbit_name_list)
        ser = self.get_serializer(result_persons, many=True)
        return Response(ser.data)


class HobbitModelViewSet(ModelViewSet):
    queryset = Hobbit.objects.all()
    serializer_class = HobbitSerializer
