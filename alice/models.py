from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models import *


# python manage.py makemigrations && python manage.py migrate

class NavigationQuerySet(QuerySet):
    def delete(self):
        for i in self:
            i.permission.delete()
        super().delete()


class NavigationManager(Manager):
    def get_queryset(self):
        return NavigationQuerySet(self.model, using=self._db)


class Navigation(Model):
    objects = NavigationManager()
    category = CharField(max_length=64)
    name = CharField(max_length=64, unique=True)
    permission = OneToOneField(Permission, on_delete=CASCADE)
    url = CharField(max_length=64, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        default = {
            "name": "can view menu " + self.name,
            "content_type": ContentType.objects.get_for_model(self),
            "codename": "view_menu_" + self.name
        }
        self.permission, _ = Permission.objects.update_or_create(
            defaults=default,
            id=self.permission.id if self.pk is not None else None
        )
        return super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.permission.delete()
        return super().delete(using, keep_parents)
