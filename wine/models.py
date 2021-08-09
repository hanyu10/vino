from django.db import models

class Country(models.Model):
    area = models.CharField(max_length=50)

    def __str__(self):
        return self.area

class Wine(models.Model):
    name = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    wine_type = models.CharField(max_length=50)
    area = models.ForeignKey(Country, on_delete=models.CASCADE)
    sugar = models.IntegerField()
    sour = models.IntegerField()

    def __str__(self):
        return self.name
