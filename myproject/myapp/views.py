from django.shortcuts import render,redirect

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('index.html')

# Create your views here.
def index(request):
    return render(request,"index.html")
