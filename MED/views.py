import json
import random
from django.shortcuts import render, redirect, get_object_or_404  # <--- FIXED THIS LINE
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Branch, Worker, Stock, Medicine, Patient

def patient_portal(request):
    branches = Branch.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        branch_id = request.POST.get('branch')
        photo = request.FILES.get('prescription')
        
        branch = Branch.objects.get(name=branch_id)
        
        # Create the order and the random 4-digit code
        order = Order.objects.create(
            patient_name=name,
            branch=branch,
            prescription_photo=photo,
            status='Pending',
            delivery_code=str(random.randint(1000, 9999))
        )
        return render(request, 'success.html', {'order': order})

    return render(request, 'patient_portal.html', {'branches': branches})
from django.db.models import Sum
from datetime import date

def branch_inventory(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    # Get all medicines in stock for this branch
    inventory = Stock.objects.filter(branch=branch)
    return render(request, 'branch_inventory.html', {
        'branch': branch,
        'inventory': inventory
    })

def branch_dashboard(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    today = date.today()

    # 1. Manage Workers at this branch
    workers = Worker.objects.filter(branch=branch, is_active=True)

    # 2. Calculate Daily Sales
    # We filter by branch and today's date
    daily_orders = Order.objects.filter(
        branch=branch, 
        created_at__date=today,
        status='Completed' 
    )
    
    # Sum up the total_price column
    total_sales = daily_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0

    return render(request, 'branch_dashboard.html', {
        'branch': branch,
        'workers': workers,
        'total_sales': total_sales,
        'order_count': daily_orders.count(),
        'recent_orders': daily_orders.order_by('-created_at')[:5]
    })

@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def approve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Approved'
    order.save()
    return redirect('order_list')

@login_required
def rider_dashboard(request):
    deliveries = Order.objects.filter(status__in=['Approved', 'In Transit'])
    return render(request, 'rider_dashboard.html', {'deliveries': deliveries})

@login_required
def track_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'track_order.html', {'order': order})

@csrf_exempt
def update_location(request, order_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            order = get_object_or_404(Order, id=order_id)
            order.latitude = data.get('lat')
            order.longitude = data.get('lng')
            order.status = 'In Transit'
            order.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'failed'}, status=400)