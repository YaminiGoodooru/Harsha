# Generated by Django 5.1 on 2024-08-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtAuctionSpaceApp', '0002_order_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pid',
            field=models.IntegerField(default=0),
        ),
    ]
