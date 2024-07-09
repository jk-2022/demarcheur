# products/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée pour permettre aux utilisateurs de modifier leurs propres produits.
    """

    def has_object_permission(self, request, view, obj):
        # Les autorisations en lecture sont autorisées pour n'importe qui
        if request.method in permissions.SAFE_METHODS:
            return True

        # Autoriser les modifications uniquement si l'utilisateur est le propriétaire du produit
        return obj.user == request.user or request.user.is_staff
