from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    ...

class IsOwnerAdminModeratorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    ...

class IsAdminOrReadOnly(permissions.BasePermission):
    ...