# Generated by Django 3.0.7 on 2020-06-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200616_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extras',
            name='pizzas',
        ),
        migrations.AddField(
            model_name='extras',
            name='pizzas_extra',
            field=models.ManyToManyField(blank=True, related_name='pizzas_extra', to='orders.Pizzas'),
        ),
    ]
