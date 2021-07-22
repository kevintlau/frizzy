# Generated by Django 3.2.5 on 2021-07-22 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=200)),
                ('security_code', models.CharField(max_length=4)),
                ('exp_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('description', models.TextField(max_length=400)),
                ('promotion', models.DecimalField(decimal_places=2, max_digits=2)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('T', 'Tub')], default='S', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('city', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1)),
                ('delivery_fee', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.creditcard')),
                ('icecreams', models.ManyToManyField(to='main_app.IceCream')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='icecream',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.shop'),
        ),
    ]
