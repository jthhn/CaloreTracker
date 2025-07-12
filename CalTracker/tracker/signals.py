from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import User_goal

@receiver(post_save, sender=User)
def create_user_goal(sender, instance, created, **kwargs):
    if created:
        User_goal.objects.create(user=instance)
        