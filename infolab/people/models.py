from django.db import models
from django.contrib.auth.models import User, UserManager


class Paper(models.Model):
    title = models.CharField(max_length=300)
    abstract = models.TextField()
    details = models.TextField()
    pdf = models.FileField(upload_to='papers/')
    def __unicode__(self): return self.title

GROUPINGS = ( ('fac', 'Faculty'),
    ('PhD', 'PhD Students'),
    ('Mas', 'Masters Students'),
    )

class Person(User):
    papers = models.ManyToManyField(Paper, null=True, blank=True) 
    twitter = models.CharField(max_length=128, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    face    = models.ImageField(upload_to='faces/', help_text="a png of about 120x120 is just about right")
    title   = models.CharField(max_length=255)
    office  = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    interests = models.TextField()
    descr  = models.TextField(blank=True, null=True)
    grouping = models.CharField(max_length=6,choices=GROUPINGS, blank=True,null=True)
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()

