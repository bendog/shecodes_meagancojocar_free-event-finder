# Generated by Django 2.2 on 2019-09-14 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0002_event_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(related_name='events', to='eventFinderApp.Category'),
        ),
    ]
