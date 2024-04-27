from django.db import models


class FoodItem_Model(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name