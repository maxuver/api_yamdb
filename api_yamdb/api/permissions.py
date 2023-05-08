from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """"IsAdmin permission allows access to the resourse only if the user is
    authenticated and has an admin/superuser role."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsOwnerAdminModeratorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """"IsOwnerAdminModeratorOrReadOnly permission allows
    access to the resourse if the user is authenticated or a safe
    method is used. Access to the object is allowed if a safe method
    is used / user is object owner or has moderator/admin/
    superuser role."""

    message = 'Изменить контент может только автор, админ или модератор.'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or request.user == obj.author)


class IsAdminOrReadOnly(permissions.BasePermission):
    """"IsAdminOrReadOnly permission allows access to the resourse
    if a safe method is used or if the user is authenticated
    and has an admin/superuser role."""

    message = 'Изменить контент может только админ.'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.is_admin))
