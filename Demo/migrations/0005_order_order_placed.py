# Generated by Django 3.2.8 on 2022-01-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0004_inventory_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_placed',
            field=models.BooleanField(default=False),
        ),
    ]
