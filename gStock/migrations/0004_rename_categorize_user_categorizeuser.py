# Generated by Django 3.2 on 2021-04-28 10:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gStock', '0003_article_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorize_User',
            new_name='CategorizeUser',
        ),
    ]
