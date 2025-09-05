from django.forms import ModelForm
from .models import User

#User creation form for receiving and processing the submitted form data

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'user_type']

class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'apartment_code', 'location_name', 'road', 'bedrooms', 'rent', 'caretaker']
        