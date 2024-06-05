from django.db import models

# Create your models here.
class Mask(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='masks/')
    
    def __str__(self):
        return self.name

class SurgicalCap(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='caps/')
    
    def __str__(self):
        return self.name

class CustomOrder(models.Model):
    product_type = models.CharField(max_length=50, choices=[('mask', 'Mask'), ('cap', 'Cap')])
    custom_text = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product_type} - {self.custom_text}"