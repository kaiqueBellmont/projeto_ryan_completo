# Generated by Django 5.0.4 on 2024-04-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_remove_event_updated_at_event_update_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userevent',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
