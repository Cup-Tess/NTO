# Generated by Django 4.0.2 on 2022-03-09 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0004_staistik_posetit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staistik',
            name='id',
        ),
        migrations.AlterField(
            model_name='staistik',
            name='exponat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='museum.sviz'),
        ),
    ]
