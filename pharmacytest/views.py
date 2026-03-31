from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pharmacy

# Create your views here.
def recipes(request):
    if request.method == 'POST':
        data = request.POST
      
        name = data.get('pharmacy_name')
        address = data.get('address')
        phone_number = data.get('phone_number')
        owner_name = data.get('owner_name')
        pharmacy_license_number = data.get('pharmacy_license_number')

        Pharmacy.objects.create(
           
            name=name,
            address=address,
            phone_number=phone_number,
            owner_name=owner_name,
            pharmacy_license_number=pharmacy_license_number
        )
        return redirect('/')

    queryset = Pharmacy.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'pharmacies': queryset}
    return render(request, 'pharmacies.html', context)


def delete_pharmacy(request, id):
    pharmacy = get_object_or_404(Pharmacy, id=id)
    pharmacy.delete()
    return redirect('/')


def update_pharmacy(request, id):
    pharmacy = get_object_or_404(Pharmacy, id=id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('pharmacy_name')
        address = data.get('address')
        phone_number = data.get('phone_number')
        owner_name = data.get('owner_name')
        pharmacy_license_number = data.get('pharmacy_license_number')

        pharmacy.name = name
        pharmacy.address = address
        pharmacy.phone_number = phone_number
        pharmacy.owner_name = owner_name
        pharmacy.pharmacy_license_number = pharmacy_license_number
        pharmacy.save()
        return redirect('/')

    context = {'pharmacy': pharmacy}
    return render(request, 'pharmacy.html', context)