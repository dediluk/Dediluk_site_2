from .models import User
from django import forms
from django.forms import ModelForm


class ChangePasswordFrom(ModelForm):
    class Meta:
        model = User
        fields = [


        ]