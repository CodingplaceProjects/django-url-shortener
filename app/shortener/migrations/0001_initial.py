# Generated by Django 4.0.1 on 2022-01-13 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenLink',
            fields=[
                ('key', models.CharField(editable=False, max_length=5, primary_key=True, serialize=False)),
                ('link', models.URLField(max_length=1000)),
            ],
        ),
    ]
