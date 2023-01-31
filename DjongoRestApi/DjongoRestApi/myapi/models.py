from email.policy import default
from django.db.models.fields import IntegerField
from djongo import models
from datetime import date
from django.utils import timezone

# Create your models here.

class Like(models.Model):
    like_id=models.IntegerField(default=0)
    Lusername=models.CharField(max_length=50)
    date=models.CharField()
    time=models.CharField()
    count=models.IntegerField(default=0)

    class Meta:
        abstract=True


class Mypost(models.Model):
    Pusername=models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    like=models.EmbeddedField(
        model_container=Like
    )
    TotalLike=models.IntegerField(default=0)

    
