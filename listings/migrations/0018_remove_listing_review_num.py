# Generated by Django 3.2.8 on 2021-11-08 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_listing_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='review_num',
        ),
    ]