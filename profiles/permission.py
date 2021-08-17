from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Permite al usuario editar su propip permiso """

    def has_object_permission(self, request, view, obj):
        """ Chequear si un usuario esta editanto su propio perfil """
        if request.method in permissions.SAFE_METHODS:
            return True

        return super().has_object_permission(request, view, obj)