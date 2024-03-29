from django.db import models

# Create your models here.


class ApiModel(models.Model):
    name = models.CharField(max_length=100)
    actual_price = models.PositiveIntegerField(default=0)
    sales_price = models.PositiveIntegerField(default=0)
    desc = models.CharField(max_length=400)
    contact = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
