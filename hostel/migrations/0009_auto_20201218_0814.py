# Generated by Django 3.1.4 on 2020-12-18 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0008_auto_20201218_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
