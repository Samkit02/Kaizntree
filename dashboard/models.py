from django.db import models
from authentication.models import CustomUser

class InventoryItem(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    stock_status = models.CharField(max_length=50)
    available_stock = models.IntegerField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
