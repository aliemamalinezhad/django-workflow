from django.db import models
from viewflow.models import Process
# Create your models here.


class Person(Process):
    name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    approved = models.BooleanField(default=False)


    
