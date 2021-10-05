from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Article
from .models import Entree
from .models import Sortie
from .models import CategorizeUser
from .models import ArticleUnit
from .models import Produit
from .models import Materiel
from .models import Supplier
# from . import api_settings

class ArticleUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleUnit
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'


class MaterielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiel
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class CategorizeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorizeUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


def get_next_entree_ref():
    l = [int(p.reference[3:]) for p in Sortie.objects.all() if p.reference[:3]=="ENT"]
    if l:
        next = max(l)+1
    else:
        next = 1
    return u"ENT" + "%09d" % next


class EntreeSerializer(serializers.ModelSerializer):
    data = serializers.CharField(
        label = "Articles",
        help_text = "Articles, Quantity & Observation",
        style={'base_template': 'textarea.html'}
    )

    class Meta:
        model = Entree
        fields = '__all__'
        # fields = ['reference', 'seller', 'client', 'data', 'amount', 'delivery_status', 'date', 'payment_status', 'payment_date']


def get_next_sortie_ref():
    l = [int(p.reference[3:]) for p in Sortie.objects.all() if p.reference[:3]=="SOR"]
    if l:
        next = max(l)+1
    else:
        next = 1
    return u"SOR" + "%09d" % next


class SortieSerializer(serializers.ModelSerializer):
    data = serializers.CharField(
        label = "Articles",
        help_text = "Articles, Quantity & Observation",
        style={'base_template': 'textarea.html'}
    )

    class Meta:
        model = Sortie
        fields = '__all__'
