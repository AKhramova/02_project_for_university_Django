from django.db import models

class Questions(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    email = models.EmailField()
    service = models.CharField(max_length=200)
    message = models.TextField("Description")