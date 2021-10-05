from rest_framework import permissions
from .models import (
                        Produit,
                         Materiel,
                         Article
                    )

ARTICLE_GROUP = ['Gestionnaires_Articles', 'Administrateurs']
PRODUIT_GROUP = ['Gestionnaires_Produits', 'Administrateurs']
MATERIEL_GROUP = ['Gestionnaires_Materiels', 'Administrateurs']
SUPPLIER_GROUP = ['Gestionnaires_Suppliers', 'Administrateurs']
ENTREE_SORTIE_GROUP = ['Gestionnaires_Entrees_Sorties', 'Administrateurs']
UTILISATEUR_GROUP = ['Utilisateurs', 'Administrateurs']

class ArticleCRUD(permissions.BasePermission):
    """
    Check if user has CRUD permission.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name in ARTICLE_GROUP:
                return True
        return False

class ArticleReadOnly(permissions.BasePermission):
    """
    Check if user is Book owner or not.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name == 'ReadOnly_Articles' and view.action == 'list':
                return True
        return False

class ProduitCRUD(permissions.BasePermission):
    """
    Check if user has CRUD permission.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name in PRODUIT_GROUP:
                return True
        return False

class ProduitReadOnly(permissions.BasePermission):
    """
    Check if user is Book owner or not.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name == 'ReadOnly_Produits' and view.action == 'list':
                return True
        return False

class MaterielCRUD(permissions.BasePermission):
    """
    Check if user has CRUD permission.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name in MATERIEL_GROUP:
                return True
        return False

class MaterielReadOnly(permissions.BasePermission):
    """
    Check if user is Book owner or not.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name == 'ReadOnly_Materiels' and view.action == 'list':
                return True
        return False


class SupplierCRUD(permissions.BasePermission):
    """
    Check if user has CRUD permission.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name in SUPPLIER_GROUP:
                return True
        return False

class SupplierReadOnly(permissions.BasePermission):
    """
    Check if user is Book owner or not.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name == 'ReadOnly_Suppliers' and view.action == 'list':
                return True
        return False
        

class EntreeSortieCRUD(permissions.BasePermission):
    """
    Check if user has CRUD permission.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name in ENTREE_SORTIE_GROUP:
                return True
        return False

class EntreeSortieReadOnly(permissions.BasePermission):
    """
    Check if user is Book owner or not.
    """
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name == 'ReadOnly_EntreesSorties' and view.action == 'list':
                return True
        return False

# reference
# class IsBookOwner(permissions.BasePermission):
#     """
#     Check if user is Book owner or not.
#     """
#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user
