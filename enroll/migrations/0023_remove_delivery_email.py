# Generated by Django 3.2.5 on 2021-08-14 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0022_delivery_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='email',
        ),
    ]