from django.db import models
from buddiaccounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
import os
from django.utils.html import mark_safe

#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
# Link to Articled that explained the process in the Models


def get_image_path(instance, filename):
    print("Triggered, this is the destination:", str(instance), filename)
    return os.path.join('photos', str(instance), filename)


class Profile(models.Model):
    """ This model Profile will be used to create A profile of the User"""
    profile_Image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    birth_month = models.CharField(max_length=2,  blank=True)
    birth_day = models.CharField(max_length=2,  blank=True)
    birth_year = models.CharField(max_length=4, blank=True)
    age = models.CharField(max_length=3, blank=True)
    seeker = models.BooleanField(default=True, blank=True)
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.email

    def image_tag(self):
        return mark_safe('<img src="/photos/%s" width="150" height="150" />' % (self.profile_Image))


@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        print("This is the instance saved", instance)
        Profile.objects.create(user=instance)
    instance.profile.save()
