from django import forms
from django.core.exceptions import ValidationError

from app_auth.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            "username": forms.TextInput(
                attrs={'placeholder': "Username"}),
            "email": forms.EmailInput(
                attrs={'placeholder': "Email"}),
            "age": forms.NumberInput(
                attrs={'placeholder': "Age",
                       'min': 0,
                       }),

        }
