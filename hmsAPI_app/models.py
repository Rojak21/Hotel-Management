from django.db import models

class UserDetails(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE,null=True)
    fullname = models.CharField(max_length=255)
    emailid = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    