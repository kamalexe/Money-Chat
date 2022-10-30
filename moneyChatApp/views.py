from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def index(request):
    try:
        if User.is_authenticated:
            print(request.session['logged_user'])
            user = User.objects.get(username=request.session['logged_user'])
            print(user.email)
            return render(request, 'index.html')
        else:
            return redirect("login")
    except:
        return redirect("login")