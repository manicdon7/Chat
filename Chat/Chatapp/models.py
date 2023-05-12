from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="img", blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name
    