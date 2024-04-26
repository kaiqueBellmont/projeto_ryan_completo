# Generated by Django 5.0.4 on 2024-04-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('deleted_at', models.DateField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'event',
                'db_table': 'event',
            },
        ),
    ]
