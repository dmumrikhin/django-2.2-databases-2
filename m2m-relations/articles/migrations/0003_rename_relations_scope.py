# Generated by Django 4.2.4 on 2023-08-08 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tags_relations_article_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Relations',
            new_name='Scope',
        ),
    ]
