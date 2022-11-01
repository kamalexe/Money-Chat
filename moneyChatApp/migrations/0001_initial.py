# Generated by Django 4.1.2 on 2022-11-01 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_Money', models.IntegerField(default=0, max_length=100)),
                ('receiver_Name', models.CharField(default=0, max_length=20)),
                ('send_Money', models.IntegerField(default=0, max_length=100)),
                ('sender_Name', models.CharField(default=0, max_length=20)),
                ('entry_Date', models.DateTimeField()),
            ],
        ),
    ]