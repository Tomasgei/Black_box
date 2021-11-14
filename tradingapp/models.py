from django.db import models
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.utils.translation import gettext as _

# Create your models here.
class User_profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE,("Male")),
        (GENDER_FEMALE,("Female")),
    ]

    # Managed fields
    user     = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar   = models.ImageField(upload_to="avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender   = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone    = models.CharField(max_length=32, null=True, blank=True)
    address  = models.CharField(max_length=255, null=True, blank=True)
    number   = models.CharField(max_length=32, null=True, blank=True)
    city     = models.CharField(max_length=50, null=True, blank=True)
    zip      = models.CharField(max_length=30, null=True, blank=True)

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('webapp/assets/img/avatar.svg')