from django import forms

from albums.models import Album
from profiles.models import Profile
from common.form_mixins import ReadonlyDisabledFieldsMixin
from common.views import get_profile


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        exclude = ('owner',)

        widgets = {
            "album_name": forms.TextInput(
                attrs={'placeholder': "Album name"}),
            "artist": forms.TextInput(
                attrs={'placeholder': "Artist"}),
            "description": forms.TextInput(
                attrs={'placeholder': "Artist"}),
            "image_URL": forms.URLInput(
                attrs={'placeholder': "Image URL"}),
            "price": forms.NumberInput(
                 attrs={'placeholder': "Price"}),

            'genre': forms.Select(choices=Album.Genre.choices),

            }

    # or override form_valid() in the view
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = get_profile() # associate the user with the instance
        if commit:
            instance.save()
        return instance


class AlbumDeleteForm(forms.ModelForm, ReadonlyDisabledFieldsMixin):
    disabled_fields = ('album_name', 'artist', 'genre', 'description', 'image_URL', 'price')

    class Meta:
        model = Album
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._mark_disabled_fields()


    #
    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #     return self.instance
