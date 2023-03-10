from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transactions(models.Model):
    time = models.DateTimeField()


class Coins(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    btc_amount = models.FloatField(default=0.00)
    ether_amount = models.FloatField(default=0.00)
    pCoin_amount = models.FloatField(default=0.00)
    # profile_image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return f"{self.owner} {self.symbol} {self.amount}"