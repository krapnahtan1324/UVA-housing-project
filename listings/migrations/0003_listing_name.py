# Generated by Django 3.2.7 on 2021-11-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listingimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='name',
            field=models.CharField(default='NO_NAME', max_length=100),
        ),
    ]