# Generated by Django 3.0.7 on 2020-06-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20200622_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizza_extra',
            field=models.ManyToManyField(blank=True, to='orders.Extra'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='progress',
            field=models.CharField(choices=[('Buon Appetito!', '1'), ('In delivery', '2'), ('We are preparing your order', '3'), ('We are cooking your pizza', '4'), ('We have received your order', '5')], default='We have received your order', max_length=256),
        ),
    ]
