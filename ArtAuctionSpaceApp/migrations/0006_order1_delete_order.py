# Generated by Django 5.1 on 2024-08-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtAuctionSpaceApp', '0005_painting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('street_address', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('card_number', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
