# Generated by Django 4.2.11 on 2024-08-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtAuctionSpaceApp', '0015_paintings_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='paintings',
            name='pid',
            field=models.IntegerField(default=0),
        ),
    ]
