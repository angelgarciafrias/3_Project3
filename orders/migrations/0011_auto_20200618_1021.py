# Generated by Django 3.0.7 on 2020-06-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200618_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizzas_extra',
            field=models.ManyToManyField(to='orders.Extra'),
        ),
    ]
