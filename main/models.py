from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.number