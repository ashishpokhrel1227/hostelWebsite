# Generated by Django 3.1.4 on 2020-12-18 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_auto_20201218_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]