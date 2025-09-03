from django.db import models

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    bedrooms = models.IntegerField(default=1)
    rent = models.IntegerField(max_digits=10)
    availability = models.TextField()

class Location(models.Model):
    county = models.CharField(max_length=100)
    subcounty = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.county}, {self.subcounty}, {self.ward}"

class Caretaker(models.Model):
    name = models.CharField(max_length=250)
    contact = models.IntegerField()
    email = models.EmailField()
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='caretaker')
