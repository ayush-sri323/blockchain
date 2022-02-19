from django import forms
from django.contrib.auth.models import User
from django.db import models
from user.models import UserProfile


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=60,  unique=True)
    transaction_amount = models.DecimalField(decimal_places=4, max_digits=10)
    posting_date = models.DateTimeField()
    settled_date = models.DateTimeField()
    status = models.IntegerField()
    