from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

gender_choice = (
    ('m', 'Male'),
    ('f', 'Female')
)

disabilities = (
    ('n', 'None'),
    ('s', 'Specify')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to = 'assets/images',
        #default = 'no-img.jpg',
        blank=True
    )
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='none@email.com')
    birth_date = models.DateField(default='1999-12-31')
    bio = models.TextField(default='')
    village = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choice)
    disabilities = models.CharField(max_length=200, choices=disabilities)
    cv = models.FileField(upload_to='files/', max_length=100)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
