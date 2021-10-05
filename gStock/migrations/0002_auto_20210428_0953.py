# Generated by Django 3.2 on 2021-04-28 09:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gStock', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrees',
            new_name='Entree',
        ),
        migrations.RenameModel(
            old_name='Sorties',
            new_name='Sortie',
        ),
        migrations.AddField(
            model_name='article',
            name='proprietaire',
            field=models.CharField(blank=True, help_text="Propriétaire de l'article.", max_length=100),
        ),
    ]
