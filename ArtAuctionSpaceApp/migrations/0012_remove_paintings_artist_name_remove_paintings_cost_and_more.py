# Generated by Django 5.1 on 2024-08-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtAuctionSpaceApp', '0011_paintings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paintings',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='paintings',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='paintings',
            name='title',
        ),
        migrations.AddField(
            model_name='paintings',
            name='artistname',
            field=models.CharField(default='Unknown Artist', max_length=255),
        ),
        migrations.AddField(
            model_name='paintings',
            name='artname',
            field=models.CharField(default='Unknown Art', max_length=100),
        ),
        migrations.AddField(
            model_name='paintings',
            name='description',
            field=models.TextField(default='No description'),
        ),
        migrations.AddField(
            model_name='paintings',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='paintings',
            name='materials',
            field=models.TextField(default='Unknown materials'),
        ),
        migrations.AddField(
            model_name='paintings',
            name='mobileno',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='paintings',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paintings',
            name='upi_id',
            field=models.CharField(default='example@upi', max_length=50),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='image',
            field=models.ImageField(default='art_images/default.jpg', upload_to='art_images/'),
        ),
    ]
