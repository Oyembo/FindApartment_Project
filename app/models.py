from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class UserType(models.TextChoices):
        TENANT = 'Tenant', 'Tenant'
        CARETAKER = 'Caretaker', 'Caretaker'
        
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.TENANT,
    )

class Tenant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.IntegerField(max_digits=10)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Caretaker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.IntegerField(max_digits=10)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Apartment(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    apartment_code = models.CharField(max_length=5)
    location_name = models.CharField(max_length=50)
    road = models.CharField(max_length=100)
    bedrooms = models.IntegerField(default=1)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE, related_name='users')

class ApartmentImage(models.Model):
    image_url = models.CharField(max_length=255)
    apartment_code = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.apartment_code}"

