from rest_framework import serializers
from .models import User, Apartment, Caretaker, ApartmentImage, Tenant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'name', 'email', 'user_type']

class TenantSerializer(serializers.ModelSerializer):
    email = UserSerializer(read_only=True)

    class Meta:
        model = Tenant
        fields = ['id', 'first_name', 'last_name', 'contact', 'email']

class CaretakerSerializer(serializers.ModelSerializer):
    email = UserSerializer(read_only=True)

    class Meta:
        model = Caretaker
        fields = ['id', 'first_name', 'last_name', 'contact', 'email']

class ApartmentImageSerializer(serializers.ModelSerializer):
    models = ApartmentImage
    fields = ['id', 'image_url']

class ApartmentSerializer(serializers.ModelSerializer):
    caretaker = CaretakerSerializer(read_only=True)
    images =ApartmentImageSerializer(source='apartmentimage_set', many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ['id', 'name', 'description', 'apartment_code', 'location_name', 'road', 'bedrooms', 'rent', 'caretaker', 'images']

