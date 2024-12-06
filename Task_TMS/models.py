from django.db import models
from django.contrib.auth.models import AbstractUser

#Cutomize abs user for email 
class User(AbstractUser):
  email= models.EmailField(unique=True)

  def __str__(self):
    return self.username
  


 