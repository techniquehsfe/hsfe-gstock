from django.shortcuts import render

from django.http import JsonResponse
from django.core import serializers

import datetime
import json

from django.shortcuts import redirect

from .models import Article, Entree, Sortie, CategorizeUser, ArticleUnit, Produit, Materiel, Supplier
from django.contrib.auth.models import User

from .serializers import ArticleSerializer
from .serializers import ArticleUnitSerializer
from .serializers import CategorizeUserSerializer
from .serializers import EntreeSerializer
from .serializers import SortieSerializer
from .serializers import UserSerializer
from .serializers import ProduitSerializer
from .serializers import MaterielSerializer
from .serializers import SupplierSerializer

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import authentication, permissions

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from .permissions import (
                            ArticleCRUD,
                            ArticleReadOnly,
                            ProduitCRUD,
                            ProduitReadOnly,
                            MaterielCRUD,
                            MaterielReadOnly,
                            SupplierCRUD,
                            SupplierReadOnly,
                            EntreeSortieCRUD,
                            EntreeSortieReadOnly,
                         )

# Create your views here.
def root(request):
    return redirect("dashboard/")

def index(request):
    return render(request, 'gStock/index.html')


def articles_queryset(request):
    data = serializers.serialize("json", Article.objects.all())
    return JsonResponse(data, safe=False)

def entrees_queryset(request):
    data = serializers.serialize("json", Entree.objects.all())
    return JsonResponse(data, safe=False)

def sorties_queryset(request):
    data = serializers.serialize("json", Sortie.objects.all())
    return JsonResponse(data, safe=False)

def categorize_users_queryset(request):
    data = serializers.serialize("json", CategorizeUser.objects.all())
    return JsonResponse(data, safe=False)

def users_queryset(request):
    data = serializers.serialize("json", User.objects.all())
    return JsonResponse(data, safe=False)




class ArticleUnitViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    queryset = ArticleUnit.objects.all()
    serializer_class = ArticleUnitSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & ArticleCRUD) | (IsAuthenticated & ArticleReadOnly)]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & ProduitCRUD) | (IsAuthenticated & ProduitReadOnly)]

    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class MaterielViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & MaterielCRUD) | (IsAuthenticated & MaterielReadOnly)]

    queryset = Materiel.objects.all()
    serializer_class = MaterielSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & SupplierCRUD) | (IsAuthenticated & SupplierReadOnly)]#[IsAuthenticated]

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CategorizeUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CategorizeUser.objects.all()
    serializer_class = CategorizeUserSerializer


class EntreeViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & EntreeSortieCRUD) | (IsAuthenticated & EntreeSortieReadOnly)]

    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer


    @action(detail=False)
    def get_entrees_objects(self, request):
        entrees = Entree.objects.all()

        for entree in entrees:
            value = entree.data

            if value == "":
                entree.data = None

            try:
                if isinstance(value, str):
                    entree.data = json.loads(value)
                if isinstance(value, list):
                    entree.data = entree.data
            except ValueError:
                pass
        serializer = self.get_serializer(entrees, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def get_last_entree(self, request):
        last_entree = Entree.objects.latest('id')

        serializer = self.get_serializer(last_entree)
        return Response(serializer.data)


class GetCurrentEntrees(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & EntreeSortieCRUD) | (IsAuthenticated & EntreeSortieReadOnly)]

    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer

    def get_queryset(self):
        today = datetime.date.today()
        qs = super().get_queryset()
        new_entree_list = []

        for entree in qs:
            if entree.date.day == today.day:
                new_entree_list.append(entree)

        return new_entree_list

class GetGlobalEntree(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & EntreeSortieCRUD) | (IsAuthenticated & EntreeSortieReadOnly)]

    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer

    def get_queryset(self):
        today = datetime.date.today()
        qs = super().get_queryset()
        new_entree_list = []

        for entree in qs:
            if entree.date.year == today.year:
                new_entree_list.append(entree)

        return new_entree_list





class SortieViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & EntreeSortieCRUD) | (IsAuthenticated & EntreeSortieReadOnly)]

    queryset = Sortie.objects.all()
    serializer_class = SortieSerializer


    @action(detail=False)
    def get_sorties_objects(self, request):
        sorties = Sortie.objects.all()

        for sortie in sorties:
            value = sortie.data

            if value == "":
                sortie.data = None

            try:
                if isinstance(value, str):
                    sortie.data = json.loads(value)
                if isinstance(value, list):
                    sortie.data = sortie.data
            except ValueError:
                pass
        serializer = self.get_serializer(sorties, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def get_last_sortie(self, request):
        last_sortie = Sortie.objects.latest('id')

        serializer = self.get_serializer(last_sortie)
        return Response(serializer.data)


class GetCurrentSorties(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & EntreeSortieCRUD) | (IsAuthenticated & EntreeSortieReadOnly)]

    queryset = Sortie.objects.all()
    serializer_class = SortieSerializer

    def get_queryset(self):
        today = datetime.date.today()
        qs = super().get_queryset()
        new_sortie_list = []

        for sortie in qs:
            if sortie.date.day == today.day:
                new_sortie_list.append(sortie)

        return new_sortie_list

class GetGlobalSortie(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [(IsAuthenticated & EntreeSortieCRUD) | (IsAuthenticated & EntreeSortieReadOnly)]

    queryset = Sortie.objects.all()
    serializer_class = SortieSerializer

    def get_queryset(self):
        today = datetime.date.today()
        qs = super().get_queryset()
        new_sortie_list = []

        for sortie in qs:
            if sortie.date.year == today.year:
                new_sortie_list.append(sortie)

        return new_sortie_list


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def currentuser(self, request):
        user = request.user

        serializer = self.get_serializer(user)
        return Response(serializer.data)
