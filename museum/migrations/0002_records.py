# Generated by Django 4.0.2 on 2022-03-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('exibitId', models.CharField(blank=True, choices=[('1', 'Экспонат 1'), ('2', 'Экспонат 2'), ('3', 'Экспонат 3'), ('4', 'Экспонат 4'), ('5', 'Экспонат 5'), ('6', 'Экспонат 6'), ('7', 'Экспонат 7'), ('8', 'Экспонат 8')], max_length=50, verbose_name='selector')),
                ('timeSpentInFrontSec', models.IntegerField(default=0)),
                ('visualFeedback', models.CharField(blank=True, choices=[('1', 'Ужасно'), ('2', 'Плохо'), ('3', 'Нормально'), ('4', 'Хорошо'), ('5', 'Восхетительно')], max_length=50, verbose_name='selector')),
                ('description', models.CharField(blank=True, choices=[('1', 'Ужасно'), ('2', 'Плохо'), ('3', 'Нормально'), ('4', 'Хорошо'), ('5', 'Восхетительно')], max_length=50, verbose_name='selector')),
                ('completeness', models.CharField(blank=True, choices=[('1', 'Ужасно'), ('2', 'Плохо'), ('3', 'Нормально'), ('4', 'Хорошо'), ('5', 'Восхетительно')], max_length=50, verbose_name='selector')),
            ],
        ),
    ]
