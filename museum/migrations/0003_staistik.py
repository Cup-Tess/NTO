# Generated by Django 4.0.2 on 2022-03-09 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0002_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staistik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visualFeedback', models.IntegerField(default=0)),
                ('description', models.IntegerField(default=0)),
                ('completeness', models.IntegerField(default=0)),
                ('timesred', models.IntegerField(default=0)),
                ('timemin', models.IntegerField(default=0)),
                ('timemax', models.IntegerField(default=0)),
                ('exponat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museum.sviz')),
            ],
        ),
    ]
