# Generated by Django 3.2.5 on 2021-08-14 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0020_auto_20210811_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='area',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='date_added',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
    ]
