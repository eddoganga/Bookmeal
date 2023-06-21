# Generated by Django 4.2.2 on 2023-06-20 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=200)),
                ('category_gif', models.CharField(max_length=200)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_choice', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='SavedCarts',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cart', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_choice', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_filling', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('order', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('time_of_order', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delivered', models.BooleanField()),
            ],
        ),
    ]
