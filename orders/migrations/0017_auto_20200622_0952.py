# Generated by Django 3.0.7 on 2020-06-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_remove_pizza_total_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
