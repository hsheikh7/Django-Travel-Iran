from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        print("Username:   ", username, "   Password:  ",password)
        user = authenticate(request, username = username, password = password)
        
        if user is not None: 
            print("Amir")
            login(request, user)
            return redirect('www.google.com')
        else: 
            print("Gorbe")

    return render(request, 'accounts/login.html') 

#def logout_view(request):
#    return 

def signup_view(request):
    return render(request, 'accounts/signup.html') 
