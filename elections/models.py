from django.db import models
from django.utils.timezone import now
from .util.time import strnow
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from .util.time import str_yearnow

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, default='User', max_length=15)
    date = models.CharField(default=str_yearnow(), max_length=10)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# user데이터 모델
class UserStudyData(models.Model):
    date = models.CharField(max_length=100, null=False, default='?')
    mathhour = models.IntegerField(default=0)
    englishhour = models.IntegerField(default=0)
    koreanhour = models.IntegerField(default=0)
    sciencehour = models.IntegerField(default=0)
    name = models.CharField(max_length=100, null=False, default='?')