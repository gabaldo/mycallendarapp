from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  authenticate 
from django.contrib.auth.decorators import login_required
from account.forms import RegistrationForm, AccountAuthenticationForm

# Create your views here.
@login_required
def homeView(request):
    return render(request, 'home.html', {})

def loginView(request):
    context = {}
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = AccountAuthenticationForm()
    context['form'] = form
    return render(request, "login.html", context)

def logoutView(request):
    logout(request)
    return redirect("login")

def registerView(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, "register.html", context)
