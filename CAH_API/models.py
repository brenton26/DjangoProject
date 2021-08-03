from django.db import models

# Create your models here.
class BlackCard(models.Model):
    text = models.CharField(max_length=200)
    pick = models.IntegerField()

    cards = models.Manager()

    def __str__(self):
        return self.text


class WhiteCard(models.Model):
    text = models.CharField(max_length=200)
    
    cards = models.Manager()

    def __str__(self):
        return self.text
