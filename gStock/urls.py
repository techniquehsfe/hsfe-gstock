"""gStock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('articles/unit', views.ArticleUnitViewSet)
router.register('articles-viewsets', views.ArticleViewSet)
router.register('categorizeUserViewSet', views.CategorizeUserViewSet)

router.register('produits-viewsets', views.ProduitViewSet)

router.register('materiels-viewsets', views.MaterielViewSet)

router.register('suppliers-viewsets', views.SupplierViewSet)

router.register('entrees-viewsets', views.EntreeViewSet)
router.register('entrees/current/entrees', views.GetCurrentEntrees)
router.register('entrees/get/global/entrees', views.GetGlobalEntree)

router.register('sorties-viewsets', views.SortieViewSet)
router.register('sorties/current/sorties', views.GetCurrentSorties)
router.register('sorties/get/global/sorties', views.GetGlobalSortie)

router.register('users-viewsets', views.UserViewSet)


urlpatterns = [
    path('drf/', include(router.urls)),


    path('', views.root, name='index_gstock'),
    path('dashboard/', views.index, name='dashboard'),
    path('produits/', views.index, name='produits'),
    path('materiels/', views.index, name='materiels'),
    path('fournisseurs/', views.index, name='fournisseurs'),
    path('stocks/', views.index, name='stocks'),
    path('entrees/', views.index, name='entrees'),
    path('sorties/', views.index, name='sorties'),
    path('login/', views.index, name='login'),

    path('articles-queryset/', views.articles_queryset, name='articles_queryset'),
    path('entrees-queryset/', views.entrees_queryset, name='entrees_queryset'),
    path('sorties-queryset/', views.sorties_queryset, name='sorties_queryset'),

    path('users-queryset/', views.users_queryset, name='users_queryset'),
    path('categorize-users-queryset/', views.categorize_users_queryset, name='categorize_users_queryset'),
]
