from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=True)
    
    create_at = models.DateField(auto_now_add=True)