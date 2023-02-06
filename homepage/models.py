from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transactions(models.Model):
    time = models.DateTimeField()


class Coins(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=5)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.owner} {self.symbol} {self.amount}"