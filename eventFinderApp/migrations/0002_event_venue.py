# Generated by Django 2.2 on 2019-09-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='Null', max_length=200),
            preserve_default=False,
        ),
    ]
