# Generated by Django 3.2 on 2021-04-29 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gStock', '0005_sortie_motif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entree',
            name='observation',
        ),
        migrations.RemoveField(
            model_name='sortie',
            name='observation',
        ),
    ]