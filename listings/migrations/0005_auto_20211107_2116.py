# Generated by Django 3.2.7 on 2021-11-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listingimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.IntegerField(),
        ),
    ]
