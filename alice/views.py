from django.db.models import Value, CharField
from django.db.models.functions import Concat
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from alice.models import Navigation
from alice.permissions import IsOwnerOrReadOnly
from alice.serializers import NavigationSerializer, NavigationSerializerForSuperUser


class NavigationModelViewSet(ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Navigation.objects.all()

    # def get_queryset(self):
    #     app_label = Navigation._meta.app_label
    #     queryset = Navigation.objects.annotate(
    #         permission_fullname=Concat(
    #             Value(app_label + "."),
    #             "permission__codename",
    #             output_field=CharField()
    #         )).filter(permission_fullname__in=self.request.user.get_all_permissions())
    #     # return cache.get_or_set(cache_key, queryset, 60)
    #     return queryset

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return NavigationSerializerForSuperUser
        else:
            return NavigationSerializer
