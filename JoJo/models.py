from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class Word(models.Model):
    wordname    =  models.CharField(max_length=50, primary_key=True)
    group       =  models.CharField(max_length=20)
    soundmark   =  models.CharField(max_length=50, null=True,blank=True)
    explanation =  models.CharField(max_length=200, null=True,blank=True)
    demo_1      =  models.CharField(max_length=100, null=True,blank=True)
    demo_1_translate = models.CharField(max_length=100, null=True, blank=True)
    demo_2      =  models.CharField(max_length=100, null=True,blank=True)
    demo_2_translate = models.CharField(max_length=100, null=True, blank=True)
    demo_3      =  models.CharField(max_length=100, null=True,blank=True)
    demo_3_translate = models.CharField(max_length=100, null=True, blank=True)


    def __unicode__(self):
        return self.wordname