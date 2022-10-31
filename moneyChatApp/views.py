from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def index(request,id):
    try:
        if User.is_authenticated:
            user = User.objects.get(username=request.session['logged_user'])
            contacts = User.objects.values()
            payload = {'user': user, 'contacts': contacts}
            if id != 'a':
                chats = User.objects.get(username=id)
                payload = {'user': user, 'contacts': contacts, 'chats': chats}
            return render(request, 'index.html', payload)
        else:
            return redirect("login")
    except:
        return redirect("login")


def chat(request, chat_id):
    try:
        print(chat_id)
        payload = {'chat': chat_id}
        return redirect(f"chat/{chat_id}", payload)
    except:
        return redirect("login")


def sendmsg(request):
    if request.method == "POST":
        amount = request.POST['amount']
        print(amount)
    return HttpResponse('SENT!')