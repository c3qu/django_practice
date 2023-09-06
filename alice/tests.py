# Create your tests here.
from unittest import TestCase, skip

from django.contrib.auth.models import Permission
from django.db.models import Case, When, Value, Count, Q

from alice.models import Navigation, Administrators
from alice.serializers import NavigationSerializer


@skip
class PermissionTest(TestCase):
    def setUp(self):
        data = {
            "主机检查": [
                {
                    "name": "主机列表",
                    "path": "/host_list",
                    "component": "HostList"
                },
                {
                    "name": "检查项列表",
                    "path": "/check_item",
                    "component": "CheckItem"
                },
                {
                    "name": "ITSM主机",
                    "path": "/itsm_host",
                    "component": "ItsmHost"

                }
            ],
            "组件安装": [
                {
                    "name": "机器列表",
                    "path": "/machine_list",
                    "component": "MachineList"

                },
                {
                    "name": "安装历史",
                    "path": "/installation_history",
                    "component": "InstallationHistory"

                },
                {
                    "name": "组件列表",
                    "path": "/software_list",
                    "component": "SoftwareList"
                }
            ]
        }
        for key in data:
            for item in data[key]:
                Navigation.objects.update_or_create({
                    "category": key,
                    "name": item["name"],
                    "path": item["path"],
                    "component": item["component"]
                }, name=item["name"])

    def test_delete_permission(self):
        # Navigation.objects.all().delete()
        self.assertTrue(Permission.objects.filter(content_type_id=11).count() == 4)


class TestAdministrators(TestCase):
    # def setUp(self):
    #     names = [1, 2, 2, 0, 0, 0]
    #     for name in names:
    #         Administrators.objects.create(
    #             name=str(name),
    #             navigation_id=32
    #         )

    # 0 未检查 1 已检查 2 检查无
    # 有一个为0的 为未检查
    # 全为已检查的或者检查无的 为已检查
    # 全为检查无的 为无需检查
    def test_admin(self):
        # self.assertTrue(Administrators.objects.all().count() == 6)
        navigation = Navigation.objects.filter(administrators__isnull=False).annotate(
            unchecked=Count("pk", filter=Q(administrators__name=0)),
            checked=Count("pk", filter=Q(administrators__name=1)),
            check_none=Count("pk", filter=Q(administrators__name=2)),
        )
        ser_data = NavigationSerializer(instance=navigation, many=True).data

        # navigation2 = Navigation.objects.all()
        # ser_data = NavigationSerializer(instance=navigation2, many=True).data

        for i in ser_data:
            print(i)
        # for i in navigation:
        #     print(i.name, i.cc)
        # print(navigation)
