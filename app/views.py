from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tenant, Caretaker, Apartment, ApartmentImage

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'user_type']

class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'description', 'apartment_code', 'location_name', 'road', 'bedrooms', 'rent', 'caretaker']

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.user_type == 'Tenant':
                Tenant.objects.create(email=user)
            elif user.user_type == 'Caretaker':
                Caretaker.objects.create(email=user)
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})

@login_required
def apartment_create(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apartment_list')
    else:
        form = ApartmentForm()
    return render(request, 'apartment_create.html', {'form': form})

@login_required
def apartment_detail(request, apartment_code):
    apartment = get_object_or_404(Apartment, apartment_code=apartment_code)
    images = ApartmentImage.objects.filter(apartment_code=apartment)
    return render(request, 'apartment_detail.html', {'apartment': apartment, 'images': images})
