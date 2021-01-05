from django.db import models

# Create your models here.
class User(models.Model):
    company = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=False)

class Ip_adress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=255, blank=True, null=True)
