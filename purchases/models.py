from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
