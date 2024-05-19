from django.contrib.auth.models import User
from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Order {self.pk}'