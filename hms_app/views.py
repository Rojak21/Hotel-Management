from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Items, UserProfile
from .forms import CreateItemForm, SigninForm, SignupForm, UpdateItemForm
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'user/index.html', {'title':'index'})

def dashboard(request):
    return render(request, 'Dashboard/product.html')

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

def delete_item(request, item_id):
    item = get_object_or_404(Items, item_id=item_id)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('menu')  # Redirect to the menu page after deletion

    return render(request, 'Dashboard/delete_item.html', {'item': item})

# def update_item(request, item_id):
#     item = get_object_or_404(Items, item_id=item_id)

#     if request.method == 'POST':
#         form = UpdateItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Item updated successfully.')
#             return redirect('menu')  # Redirect to the menu page after form submission
#         else:
#             messages.error(request, 'Error updating item. Please check the form.')
#     else:
#         form = UpdateItemForm(instance=item)

#     return render(request, 'Dashboard/product.html', {'form': form, 'item': item})

def update_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        item = get_object_or_404(Items, pk=item_id)
        form = UpdateItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        # Handle other HTTP methods or redirect
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})