# Generated by Django 4.0.2 on 2022-03-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0007_alter_staistik_completeness_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staistik',
            name='Zal_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='staistik',
            name='Zal_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='staistik',
            name='Zal_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sviz',
            name='zal',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=50, verbose_name='selector'),
        ),
    ]