from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('main:home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
# Create your views here.
