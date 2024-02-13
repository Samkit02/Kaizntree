from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    security_question = models.CharField(max_length=255)
    security_answer = models.CharField(max_length=255)
