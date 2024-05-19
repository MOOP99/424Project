from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from .models import Plant, Order
from .forms import PlantForm, RegisterForm
from django.contrib import messages
from django.views.generic import UpdateView



User = get_user_model()

def plant_management(request):
    plants = Plant.objects.all()
    if request.method == 'POST':
        plant_id = request.POST.get('plant_id')
        if plant_id:
            plant = get_object_or_404(Plant, id=plant_id)
            if request.POST.get('action') == 'delete':
                plant.delete()
                return redirect('plant_management')
        else:
            form = PlantForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('plant_management')
    else:
        form = PlantForm()
    return render(request, 'plant_management.html', {'plants': plants, 'form': form})
 

def order_management(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            if request.POST.get('action') == 'delete':
                order.delete()
                return redirect('orders')
        else:
            form = PlantForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('orders')
    else:
        form = PlantForm()
    return render(request, 'orders.html', {'orders': orders, 'form': form})
 

@login_required
def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    total_price = sum(order.plant.price for order in orders)
    context = {
        'orders': orders,
        'total_price': total_price,
    }
    return render(request, 'orders.html', context)
    
    
   
def add_plant(request):
    plants = Plant.objects.all()
    if request.method == 'POST':
        plant_id = request.POST.get('plant_id')
        if plant_id:
            plant = get_object_or_404(Plant, id=plant_id)
            if request.POST.get('action') == 'delete':
                plant.delete()
                return redirect('plant_management')
        else:
            form = PlantForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('plant_management')
    else:
        form = PlantForm()
    return render(request, 'add_plant.html', {'form': form})   


def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_management')
    else:
        form = PlantForm(instance=plant)

    return render(request, 'update_plant.html', {'form': form})

           
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form}) 
             

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('plants')
        error = 'Invalid username or password'
        return render(request, 'login.html', {'form': form, 'error': error})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')


class MainView(ListView):
    model = Plant
    template_name = 'main.html'
    context_object_name = 'plants'
   
   
class PlantView(ListView):
    model = Plant
    template_name = 'plants.html'
    context_object_name = 'plants'
   

def display_plant_details(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    return render(request, 'plant_details.html', {'plant': plant})

       
       
class AddToCartView(View):
    def post(self, request, plant_id):
        plant = get_object_or_404(Plant, id=plant_id)
        order = Order.objects.create(user=request.user, plant=plant)
        order.save()
        return redirect('orders')

@login_required
def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    total_price = sum(order.plant.price for order in orders)
    context = {
        'orders': orders,
        'total_price': total_price,
    }
    return render(request, 'orders.html', context)