# Create your tests here.
from unittest import TestCase

from django.contrib.auth.models import Permission

from alice.models import Navigation


class PermissionTest(TestCase):
    def setUp(self):
        data = {
            "主机检查": [
                {
                    "name": "主机列表",
                    "url": "/host_list"
                },
                {
                    "name": "检查项列表",
                    "url": "/check_item"
                },
                {
                    "name": "ITSM主机",
                    "url": "/itsm_host"
                }
            ],
            "组件安装": [
                {
                    "name": "机器列表",
                    "url": "/machine_list"
                },
                {
                    "name": "安装历史",
                    "url": "/installation_history"
                },
                {
                    "name": "组件列表",
                    "url": "/software_list"
                }
            ]
        }
        for key in data:
            for item in data[key]:
                Navigation.objects.update_or_create({
                    "category": key,
                    "name": item["name"],
                    "url": item["url"]
                }, name=item["name"])

    def test_delete_permission(self):
        Navigation.objects.all().delete()
        self.assertTrue(Permission.objects.filter(content_type_id=11).count() == 4)