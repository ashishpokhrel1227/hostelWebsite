# Generated by Django 3.1.4 on 2020-12-18 02:13

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0003_auto_20201218_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='NE'),
        ),
    ]