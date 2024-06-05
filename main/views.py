from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main/home.html')

def cars(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'main/cars.html', context)

def car(request, id):
    car = Car.objects.get(id=id)
    context = {'car': car}
    return render(request, 'main/car.html', context)
@login_required
def new_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            new_car=form.save(commit=False)
            new_car.owner=request.user
            new_car.save()
            return redirect('main:cars')
    else:
        form = CarForm()
    context = {'form': form}
    return render(request, 'main/new_car.html', context)

@login_required
def edit_car(request, id):
    car = Car.objects.get(id=id)
    if car.owner != request.user:
        return redirect('main:cars')

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('main:car', id=id)
    else:
        form = CarForm(instance=car)
    context = {'form': form, 'car': car}
    return render(request, 'main/edit_car.html', context)

@login_required
def profile(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'main/profile.html', context)
@login_required
def delete_car(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('main:cars')

# Create your views here.
