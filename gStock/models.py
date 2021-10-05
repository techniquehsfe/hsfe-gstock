from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.

#####################
# Categorize_User
#####################
class CategorizeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=100,
        help_text="Catégorie : Employee/Prestataire/Client/etc",
    )
    date = models.DateTimeField(# date is the Creation Date
        "Date De Création",
        auto_now_add = True
    )


#####################
# Supplier
#####################
class Supplier(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Full name of supplier",
        unique=True,
    )
    phoneNumber = models.CharField(
        "Phone Number",
        max_length=20
    )
    fax = models.CharField(
        max_length=20,
        blank=True
    )
    email = models.EmailField(
        "E-Mail",
        blank=True,
        help_text="E-mail",
    )
    site_web = models.CharField(
        max_length=200,
        help_text="Le site web du fournisseur",
        blank=True,
    )
    description = models.CharField(
        max_length=500,
        blank=True,
        help_text="Mention the products that the supplier sells, its area of intervention, etc."
    )
    date = models.DateTimeField(# date is the Creation Date
        "Date De Création",
        auto_now_add = True
    )

    class Meta:
        ordering = ["name",]
        unique_together = ["name"]

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


#####################
# Articles
#####################
def validate_ean(value):
    if not len(value)==12:
        raise ValidationError(u"Le code EAN %s n'a pas la longueur requise (12)" % value)


def get_next_ean():
    l = [int(p.ean[3:]) for p in Article.objects.all() if p.ean[:3]=="ART"]
    if l:
        next = max(l)+1
    else:
        next = 1
    return u"ART" + "%09d" % next


class ArticleUnit(models.Model):
    name = models.CharField(
        "Unit",
        max_length=50,
        help_text="Article Unit"
    )
    date = models.DateTimeField(# date is the Creation Date
        "Date De Création",
        auto_now_add = True
    )

    class Meta:
        ordering = ["name"]
        unique_together = ["name",]

    def __str__(self):
        return "{}".format(self.name)


class Article(models.Model):
    name = models.CharField(
        "Name",
        max_length=200,
        help_text="Nom complet de l'article"
    )
    articleModel = models.CharField(
        "Model",
        max_length=200,
        help_text="Modèle de l'article"
    )
    reference = models.CharField(
        max_length=50,
        blank=True,
        help_text="La référence de l'article ou le numéro de série."
    )
    ean = models.CharField(
        max_length=12,
        validators=[validate_ean,],
        unique=True,
        default=get_next_ean,
        help_text="The EAN13 code for the product, i.e. 12 digits. Proposed automatically. Should start with ART for internal codes."
    )
    stock = models.IntegerField(
        help_text="La quantité d'articles en stock"
    )
    unit = models.ForeignKey(
        ArticleUnit,
        on_delete=models.CASCADE
    )
    threshold = models.IntegerField(# seuil
        default=5,
        help_text="Threshold from which to automatically replenish the product"
    )
    proprietaire = models.CharField(
        max_length=100,
        help_text="Propriétaire de l'article."
    )
    position = models.TextField(
        max_length=1000,
        blank=True,
        help_text="La position de l'article informe sur l'endroit où se trouve ce dernier."
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
        help_text="Description de l'article. Mentionner l'état defectueux ou non de l'article."
    )
    date = models.DateTimeField(# date is the Creation Date
        "Date De Création",
        auto_now_add = True
    )

    class Meta:
        ordering = ["name", "reference"]
        unique_together = ["name", "articleModel", "unit"]

    def __unicode__(self):
        return self.reference
    # def __unicode__(self):
    #     return self.name

    # def __str__(self):
    #     return self.reference
    def __str__(self):
        return "{}".format(self.name)


#####################
# Produit
#####################
class Produit(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=100,
        default="Produit",
        help_text="Produit",
    )
    buying_price = models.DecimalField(
        "Buying price",
        max_digits=20,
        decimal_places=2,
    )
    selling_price = models.DecimalField(
        "Sell price",
        max_digits=20,
        decimal_places=2,
    )
    tva = models.DecimalField(
        "Taux de TVA",
        max_digits=3,
        decimal_places=2,
        default=0.18,
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(# date is the Creation Date
        "Date De Création",
        auto_now_add = True
    )


#####################
# Materiel
#####################
class Materiel(models.Model):
    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE
    )
    category = models.CharField(
        max_length=100,
        default="Materiel",
        help_text="Produit",
    )
    date = models.DateTimeField(# date is the Creation Date
        "Date De Création",
        auto_now_add = True
    )


############################
# Mouvements Entrées-Sortie
############################
def get_next_entrees_ref():
    l = [int(p.reference[3:]) for p in Entree.objects.all() if p.reference[:3]=="ENT"]
    if l:
        next = max(l)+1
    else:
        next = 1
    return u"ENT" + "%09d" % next

def get_next_sorties_ref():
    l = [int(p.reference[3:]) for p in Sortie.objects.all() if p.reference[:3]=="SOR"]
    if l:
        next = max(l)+1
    else:
        next = 1
    return u"SOR" + "%09d" % next


class Entree(models.Model):
    reference = models.CharField(
        "Reference",
        max_length = 12,
        unique = True,
        default = get_next_entrees_ref,
        help_text = "Référence",
    )
    gestionnaire = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
    )
    demandeur = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='+',
    )
    data = models.TextField(
        "Articles",
    )
    date = models.DateTimeField(# date is the Creation Date
        "Date De Création",
        auto_now_add = True
    )


class Sortie(models.Model):
    reference = models.CharField(
        "Reference",
        max_length = 12,
        unique = True,
        default = get_next_sorties_ref,
        help_text = "Référence",
    )
    gestionnaire = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
    )
    demandeur = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='+',
    )
    data = models.TextField(
        "Articles",
    )
    motif = models.TextField(
        "Motif",
    )
    date = models.DateTimeField(# date is the Creation Date
        "Date De Création",
        auto_now_add = True
    )


############################
# Mouvements Event Log
############################
# def get_next_eventlog_ref():
#     l = [int(p.reference[3:]) for p in EventLog.objects.all() if p.reference[:3]=="LOG"]
#     if l:
#         next = max(l)+1
#     else:
#         next = 1
#     return u"LOG" + "%09d" % next
#
# class EventLog(models.Model):
#     reference = models.CharField(
#         "Reference",
#         max_length = 12,
#         unique = True,
#         default = get_next_eventlog_ref,
#         help_text = "Référence du Event_Log",
#     )
#     referenceMouvement = models.CharField(
#         "Référence Mouvement",
#         max_length = 12,
#     )
#     action = models.CharField(
#         "Action",
#         max_length = 50,
#         help_text = "Action effectuée : creation, modification, suppression",
#     )
#     date = models.DateTimeField(# date is the Creation Date
#         "Date De Création",
#         auto_now_add = True
#     )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=Article)
def autoReajustArticleEAN(sender, instance, created, *args, **kwargs):
    if created:
        instance.ean = u'ART' + "%09d" % instance.id
        instance.save(update_fields=['ean'])


@receiver(post_save, sender=Entree)
def autoReajustEntreereference(sender, instance, created, *args, **kwargs):
    if created:
        instance.reference = u'ENT' + "%09d" % instance.id
        instance.save(update_fields=['reference'])


@receiver(post_save, sender=Sortie)
def autoReajustSortiereference(sender, instance, created, *args, **kwargs):

    # log_ref = get_next_eventlog_ref()
    # log = EventLog(reference=log_ref, referenceMouvement="", action="Création", date=timezone.now())

    if created:
        instance.reference = u'SOR' + "%09d" % instance.id
        instance.save(update_fields=['reference'])

        # log.referenceMouvement = instance.reference
        # log.create()


# @receiver(post_save, sender=EventLog)
# def autoReajustEventLogreference(sender, instance, created, *args, **kwargs):
#     if created:
#         instance.reference = u'LOG' + "%09d" % instance.id
#         instance.save(update_fields=['reference'])
