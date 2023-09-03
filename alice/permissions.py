from rest_framework import permissions


class MosPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        print(view.action)
        # ip_addr = request.META['REMOTE_ADDR']
        # blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
        return True


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        app_label = obj._meta.app_label
        return app_label + "." + obj.permission.codename in request.user.get_all_permissions()
