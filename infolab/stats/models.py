from django.db import models


FlagValues = (
    (0, 'finished'),
    (1, 'started'),
    (2, 'running 01'),
    (3, 'running 02'),
    (4, 'running 03'),
    (5, 'running 04'),
    (6, 'running 05'),
    (7, 'running 06'),
    (8, 'running 07'),
    (-1, 'error'),
    (-2, 'error 01'),
    (-3, 'error 02'),
    (-4, 'error 03'),
    )


class StatFlag(models.Model):
    flag_name = models.CharField(max_length=16)
    flag_value = models.IntegerField(choices=FlagValues, default=0)
    stat_text = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    expires = models.IntegerField(default=120)


class StatKey(models.Model):
    term = models.CharField(max_length=16)
    descr = models.CharField(max_length=160, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class StatPoint(models.Model):
    statkey = models.ForeignKey(StatKey)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

