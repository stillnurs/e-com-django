# Generated by Django 3.2.2 on 2021-05-09 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='count',
            new_name='quantity',
        ),
    ]
