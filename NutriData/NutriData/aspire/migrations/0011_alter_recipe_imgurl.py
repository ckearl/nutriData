# Generated by Django 4.1.2 on 2022-12-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspire', '0010_alter_recipe_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='imgUrl',
            field=models.URLField(max_length=1000),
        ),
    ]
