from django.contrib import admin
from .models import Transactions, Coins
# Register your models here.

admin.site.register(Transactions)
admin.site.register(Coins)