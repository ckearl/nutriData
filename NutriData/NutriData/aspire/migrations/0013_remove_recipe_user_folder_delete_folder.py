# Generated by Django 4.1.2 on 2022-12-09 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aspire', '0012_alter_recipe_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe_user',
            name='folder',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
    ]
