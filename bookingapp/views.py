from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'index.html')



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
        else:
            error_message = "Invalid username or password."
            return render(request, 'admin_login.html', {'error_message': error_message})
    else:
        return render(request, 'admin_login.html')