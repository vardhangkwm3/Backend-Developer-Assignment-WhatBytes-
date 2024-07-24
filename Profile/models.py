from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WatchOver(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateField(auto_now_add=True)
    Last_used = models.DateTimeField()
