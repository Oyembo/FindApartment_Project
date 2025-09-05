from rest_framework import viewsets
from .models import User, Apartment, Caretaker, Tenant
from .serializers import UserSerializer, ApartmentSerializer, CaretakerSerializer, TenantSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CaretakerViewSet(viewsets.ModelViewSet):
    queryset = Caretaker.objects.all()
    serializer_class = CaretakerSerializer

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
