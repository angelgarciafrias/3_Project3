# Generated by Django 3.0.7 on 2020-06-22 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_remove_pizza_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='total_order',
        ),
    ]
