# Generated by Django 4.0.2 on 2022-03-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0014_marshrut'),
    ]

    operations = [
        migrations.AddField(
            model_name='marshrut',
            name='now',
            field=models.IntegerField(default=0),
        ),
    ]
