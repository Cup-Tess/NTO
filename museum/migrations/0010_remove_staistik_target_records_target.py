# Generated by Django 4.0.2 on 2022-03-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0009_staistik_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staistik',
            name='target',
        ),
        migrations.AddField(
            model_name='records',
            name='target',
            field=models.FileField(default='/static/img/met.zpt', upload_to='upload/'),
        ),
    ]
