from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ledger(models.Model):
    receive_Money = models.IntegerField(default=0)
    receiver_Name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver_Name")
    send_Money = models.IntegerField(default=0)
    sender_Name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_Name")
    entry_Date = models.DateTimeField()
