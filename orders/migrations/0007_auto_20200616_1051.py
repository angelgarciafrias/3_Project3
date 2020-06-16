# Generated by Django 3.0.7 on 2020-06-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200616_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzas',
            name='pizza_extra',
        ),
        migrations.AddField(
            model_name='extras',
            name='pizzas',
            field=models.ManyToManyField(blank=True, related_name='pizzas', to='orders.Pizzas'),
        ),
    ]
