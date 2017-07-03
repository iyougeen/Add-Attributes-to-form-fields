from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Feedback(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  text = models.TextField()

  def __str__(self):
    return self.name