from django.contrib import admin

from .models import Article, Entree, Sortie, ArticleUnit, CategorizeUser, Produit, Materiel, Supplier

# Register your models here.
class CategorizeUserAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "category", "date"]

class ArticleUnitAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "date"]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "articleModel", "reference", "ean", "stock", "unit", "threshold", "proprietaire", "position", "description", "date"]

class ProduitAdmin(admin.ModelAdmin):
    list_display = ["pk", "article", "category", "buying_price", "selling_price", "tva", "supplier", "date"]

class MaterielAdmin(admin.ModelAdmin):
    list_display = ["pk", "article", "category", "date"]

class SupplierAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "phoneNumber", "fax", "email", "site_web", "description", "date"]

class EntreeAdmin(admin.ModelAdmin):
    list_display = ["pk", "reference", "gestionnaire", "demandeur", "data", "date"]

class SortieAdmin(admin.ModelAdmin):
    list_display = ["pk", "reference", "gestionnaire", "demandeur", "data", "motif", "date"]


admin.site.register(CategorizeUser, CategorizeUserAdmin)

admin.site.register(ArticleUnit, ArticleUnitAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Materiel, MaterielAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Entree, EntreeAdmin)
admin.site.register(Sortie, SortieAdmin)
