from django import forms

from cars.form_mixins import ReadonlyFieldsMixin
from cars.models import Car
from common.views import get_profile


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

        widgets = {
            "imageURL": forms.URLInput(
                attrs={'placeholder': "https://..."}),

            'type': forms.Select(choices=Car.CarTypes.choices),
        }
        labels = {
            "imageURL": "Image URL",
        }

    # or override form_valid() in the view
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = get_profile()  # associate the user with the instance
        if commit:
            instance.save()
        return instance


class CarDeleteForm(forms.ModelForm, ReadonlyFieldsMixin):
    readonly_fields = ('model', 'year', 'imageURL', 'price')
    disabled_fields = ('type',)  # because is a choice field

    class Meta:
        model = Car
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._mark_readonly_fields()
        self._mark_disabled_fields()
