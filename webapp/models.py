from django.db import models
from django.utils import timezone

class Record(models.Model):
    flight_number = models.CharField(max_length=10)
    airways_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.flight_number} - {self.airways_name}'
