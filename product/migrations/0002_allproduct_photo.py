# Generated by Django 2.2 on 2020-07-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproduct',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='assetphoto'),
        ),
    ]