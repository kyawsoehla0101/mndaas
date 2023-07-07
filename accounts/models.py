from django.db import models
from django.contrib.auth.models import AbstractUser


LANGUAGES_CHOICES = (
    ("English", "English"),
    ("China", "China"),
    ("Myanmar", "Myanmar"),
    )


# Create your models here.
# Create your models here.
class CustomUser(AbstractUser):
    username=models.CharField(max_length=20,null=True,unique=True)
    languages = models.CharField(
        max_length = 20,
        choices = LANGUAGES_CHOICES,
        default = 'English'
        )
    
    def __str__(self):
        return self.username
    
    REQUIRED_FILEDS=['username','english','china','myanmar']
    USERNAME_FIELDS='username'
