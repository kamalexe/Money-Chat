# Generated by Django 4.1.2 on 2022-11-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyChatApp', '0002_alter_ledger_receiver_name_alter_ledger_sender_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='receive_Money',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='send_Money',
            field=models.IntegerField(default=0),
        ),
    ]
