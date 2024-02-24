from django import forms

from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')

        widgets = {
            "password": forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            "password": forms.TextInput(
                attrs={'maxlength': 200},
            ),
        }

        labels = {
            "profile_picture": "Profile Picture",
        }
