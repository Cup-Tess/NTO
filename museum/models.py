from django.db import models
from django.conf import settings

class Sviz(models.Model):
    ZALS = (
        ("1", "1"),
        ("2", "2"),
        ("3","3"),
    )
    Id_title = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='img/', default=('/static/img/аист.jpg'))
    zametki = models.CharField(max_length=200, default=" ")
    one = models.IntegerField(default=0)
    two = models.IntegerField(default=0)
    three = models.IntegerField(default=0)
    four = models.IntegerField(default=0)
    five = models.IntegerField(default=0)
    six = models.IntegerField(default=0)
    seven = models.IntegerField(default=0)
    eight = models.IntegerField(default=0)
    zal = models.CharField(max_length=50, choices=ZALS, verbose_name="selector", blank=True)
    target = models.FileField(upload_to='img/', default=('/static/img/met.zpt'))

class Records(models.Model):
    SELECTOR_EXIBIT = (
        ('1', 'Экспонат 1'),
        ('2', 'Экспонат 2'),
        ('3', 'Экспонат 3'),
        ('4', 'Экспонат 4'),
        ('5', 'Экспонат 5'),
        ('6', 'Экспонат 6'),
        ('7', 'Экспонат 7'),
        ('8', 'Экспонат 8'),
    )
    SELECTOR_MARK = (
        ('1', 'Ужасно'),
        ('2', 'Плохо'),
        ('3', 'Нормально'),
        ('4', 'Хорошо'),
        ('5', 'Восхетительно'),
    )
    id = models.IntegerField(primary_key = True)
    time = models.CharField(max_length=100, blank=True, null=True)
    exibitId = models.CharField(max_length=50, choices=SELECTOR_EXIBIT, verbose_name="selector", blank=True)
    timeSpentInFrontSec = models.IntegerField(default=0)
    visualFeedback = models.CharField(max_length=50, choices=SELECTOR_MARK, verbose_name="selector", blank=True)
    description = models.CharField(max_length=50, choices=SELECTOR_MARK, verbose_name="selector", blank=True)
    completeness = models.CharField(max_length=50, choices=SELECTOR_MARK, verbose_name="selector", blank=True)

class Staistik(models.Model):
    exponat = models.ForeignKey(Sviz, on_delete=models.CASCADE, primary_key = True)
    visualFeedback = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    description = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    completeness = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    posetit = models.IntegerField(default=0)
    timesred = models.IntegerField(default=0)
    timemin = models.IntegerField(default=0)
    timemax = models.IntegerField(default=0)
    Zal_1 = models.IntegerField(default=0)
    Zal_2 = models.IntegerField(default=0)
    Zal_3 = models.IntegerField(default=0)


class marshrut(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    way = models.CharField(max_length=100, blank=True, null=True)
    now = models.IntegerField(default=0)

