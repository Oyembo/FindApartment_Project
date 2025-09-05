from django.shortcuts import render
from .models import User, Tenant, Caretaker, Apartment, ApartmentImage
from django.forms import ModelForm, UserForm, ApartmentForm

# Create your views here.
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

def apartment_create(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apartment_list')
    else:
        form = ApartmentForm()
    return render(request, 'apartment_create.html', {'form': form})

def apartment_detail(request, apartment_code):
    apartment = get_object(Apartment, apartment_code=apartment_code)
    images = ApartmentImage.objects.filter(apartment_code=apartment)
    return render(request, 'apartment_detail.html', {'apartment': apartment, 'images': images})