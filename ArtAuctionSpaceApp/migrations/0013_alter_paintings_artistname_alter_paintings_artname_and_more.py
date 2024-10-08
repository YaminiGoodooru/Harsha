# Generated by Django 5.1 on 2024-08-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtAuctionSpaceApp', '0012_remove_paintings_artist_name_remove_paintings_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paintings',
            name='artistname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='artname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='image',
            field=models.ImageField(upload_to='art_images/'),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='materials',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='mobileno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='upi_id',
            field=models.CharField(max_length=50),
        ),
    ]
