from rest_framework import permissions


class AuthorReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
