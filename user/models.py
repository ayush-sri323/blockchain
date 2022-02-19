from django import forms
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_id = models.CharField(max_length=60,  unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    role = models.IntegerField()
    city = models.CharField(max_length=80)
    country = models.IntegerField()
    pin = models.IntegerField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(('email address'), unique=True)


class KYCDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    aadhar_number = models.IntegerField(null=False, unique=True)
    pan = models.CharField(max_length=12, null=False, unique=True)
    kyc_status = models.IntegerField()


class BankDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=80, null=False)
    bank_address = models.CharField(max_length=80)
    branch_code = models.CharField(max_length=80)
    ifsc = models.CharField(max_length=80, null=False)
    account_number = models.IntegerField(null=False, unique=True)
    swift_code = models.CharField(max_length=80)
    is_active = models.BooleanField()