from django.db import models
from datetime import datetime
# Create your models here.
class Questions(models.Model):
    qn = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=200)
