# Generated by Django 3.2.4 on 2021-07-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210724_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='promotion',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
