from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    adoption_date = models.CharField(max_length=100, blank=True, null=True)
    breed = models.CharField(max_length=100, blank=True, null=True)
    breed_group = models.CharField(max_length=100, blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    life_span = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)

    dogs = models.Manager()

    def __str__(self):
        return self.name


class TempDog(models.Model):
    breed = models.CharField(max_length=100, blank=True, null=True)
    breed_group = models.CharField(max_length=100, blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    life_span = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)

    dogs = models.Manager()


