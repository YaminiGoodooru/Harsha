# Generated by Django 5.1 on 2024-08-28 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArtAuctionSpaceApp', '0016_paintings_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paintings',
            old_name='price',
            new_name='cost',
        ),
    ]
