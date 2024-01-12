from datetime import date, timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Items, Orders, UserProfile
from .forms import CreateItemForm, CreateOrderForm, SigninForm, SignupForm, UpdateItemForm
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'user/index.html', {'title':'index'})

def dashboard(request):
    return render(request, 'Dashboard/dashboard.html')

def aboutus(request):
    return render(request, 'user/about.html')

# Example
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. You can now sign in.')
            return redirect('signin')
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = SignupForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'register here'})

def signin(request):
    if request.method == 'POST':
        emailid = request.POST['emailid']
        password = request.POST['password']
    # Assuming you have a User model with fields 'username' and 'password'
        try:
            user = UserProfile.objects.get(emailid=emailid)
            if check_password(password, user.password):
                # Passwords match, log the user in
                # You may set a session variable or create a custom session mechanism
                return redirect('dashboard')  # Replace 'home' with the name of your home view
            else:
                # Passwords do not match, show an error
                return render(request, 'user/login.html', {'error': 'Invalid password'})
        except UserProfile.DoesNotExist:
            # User does not exist, show an error
            return render(request, 'user/login.html', {'error': 'User does not exist'})
    return render(request, 'user/login.html')

def menu(request):
    menu_items = Items.objects.all()
    return render(request, 'Dashboard\product.html', {'menu_items': menu_items})

def item_list(request):
    menu_items = Items.objects.all()
    return render(request, 'Dashboard\item_list.html', {'menu_items': menu_items})

def Create_item(request):
    menu_items = Items.objects.all()
    
    if request.method == 'POST':
        form = CreateItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            print(f'Item saved: {item}')
            messages.success(request, 'Item created successfully.')
            return redirect('menu')  # Redirect to the menu page after form submission
        else:
            logger.error(f"Form errors: {form.errors}")
            print(f'Form errors: {form.errors}')
    else:
        form = CreateItemForm()

    return render(request, 'Dashboard\product.html', {'menu_items': menu_items, 'form': form})

def update_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        item = get_object_or_404(Items, pk=item_id)
        form = UpdateItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Updated successfully.')
            return redirect('item_list')
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        # Handle other HTTP methods or redirect
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        order = get_object_or_404(Items, pk=item_id)
        order.delete()
        return redirect('item_list')  # Redirect to a suitable page after deletion
    else:
        return render(request, 'Dashboard/order.html') 


def create_orders(request):
    items = Items.objects.all()
    orders = Orders.objects.all()

    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, 'Order created successfully.')
            return redirect('create_orders')  # Redirect to the same page after form submission
        else:
            logger.error(f"Form errors: {form.errors}")
            messages.error(request, 'Error creating order. Please check the form data.')
    else:
        form = CreateOrderForm()

    return render(request, 'Dashboard/order.html', {'items': items, 'orders': orders, 'form': form})

def update_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('id')
        order = get_object_or_404(Orders, pk=order_id)
        form = CreateOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully.')
            return redirect('create_orders')
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        # Handle other HTTP methods or redirect
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('id')
        order = get_object_or_404(Orders, pk=order_id)
        order.delete()
        messages.success(request, 'Order deleted successfully.')
        return redirect('create_orders')  # Redirect to a suitable page after deletion
    else:
        return render(request, 'Dashboard/order.html') 
    