from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from alice.models import Person, Hobbit, Job, PersonAndJob
from alice.serializers import PersonSerializer, HobbitSerializer, JobSerializer, PersonAndJobSerializer


# Create your views here.
class PersonModelViewSet(ModelViewSet):
    search_fields = ["sex", "name"]
    filterset_fields = ["sex", "name"]
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


class JobModelViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class PersonAndJobModelViewSet(ModelViewSet):
    filterset_fields = ["person"]
    queryset = PersonAndJob.objects.all()
    serializer_class = PersonAndJobSerializer

    @action(detail=False, methods=["get"])
    def get_all_job(self, request):
        person_id = request.GET.get("person")
        # 校验person_id是否存在
        person = None
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist as e:
            raise Exception(e)
        # 获取所有的job
        all_job = Job.objects.all()
        # 遍历所有职业并在person_and_job表中查询或者创建
        person_and_job_list = []
        for job in all_job:
            data = {
                "person": person,
                "job": job
            }
            person_and_job, _ = PersonAndJob.objects.get_or_create(defaults=data, job=job.id, person=person.id)
            person_and_job_list.append(person_and_job)
        ser = PersonAndJobSerializer(person_and_job_list, many=True)
        return Response(ser.data)

    @action(detail=False, methods=["get"])
    def get_all_job2(self, request):
        person_id = request.GET.get("person")
        # 校验person_id是否存在
        person = None
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist as e:
            raise Exception(e)
        # 获取跟这个person没有关联的职业
        all_job = Job.objects.all().exclude(personandjob__person=person)
        if all_job.exists():
            # 在person_and_job表中批量插入没有关联的职业
            person_and_job_map = map(lambda i: PersonAndJob(person=person, job=i), all_job)
            PersonAndJob.objects.bulk_create(person_and_job_map)
        # 查询this person关联的person_and_job表
        all_person_job = PersonAndJob.objects.filter(person=person_id)
        ser = PersonAndJobSerializer(all_person_job, many=True)
        return Response(ser.data)
