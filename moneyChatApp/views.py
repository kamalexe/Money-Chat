from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.models import User, auth
from .models import ledger


# Create your views here.
def index(request, id):
    try:
        if User.is_authenticated:
            user = User.objects.get(username=request.session['logged_user'])
            contacts = User.objects.values()
            payload = {'user': user, 'contacts': contacts}
            if id != 'a':
                chats = User.objects.get(username=id)
                ledgers = ledger.objects.all()
                print(ledgers)
                payload = {'user': user, 'contacts': contacts, 'chats': chats, 'ledgers': ledgers}
            return render(request, 'index.html', payload)
        else:
            return redirect("login")
    except:
        return redirect("login")


def sendmsg(request):
    if request.method == "POST":
        receiver_Name = request.POST['receive_Money']
        sender_Name = request.POST['sender_Name']
        send_Money = request.POST['amount']
        entry_Date = datetime.now()
        try:
            receiver_Name = User.objects.get(username=receiver_Name)
            sender_Name = User.objects.get(username=sender_Name)
        except Exception as e:
            print(e)
        products = ledger.objects.create(receiver_Name=receiver_Name, send_Money=send_Money, sender_Name=sender_Name, entry_Date=entry_Date)
    return redirect(f'/home/{receiver_Name}')
