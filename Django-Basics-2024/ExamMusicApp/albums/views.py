from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from albums.forms import AlbumForm, AlbumDeleteForm
from albums.models import Album



# Create your views here.
class CreateAlbumView(views.CreateView):
    form_class = AlbumForm
    template_name = 'album-add.html'
    success_url = reverse_lazy('home')

    # or save() in form -> to save additional fields
    # def form_valid(self, form):
    #     form.instance.owner_id = get_profile().pk
    #
    #     return super().form_valid(form)


class AlbumDetailsView(views.DetailView):
    model = Album  # or queryset
    template_name = "album-details.html"


class AlbumEditView(views.UpdateView):
    model = Album  # or queryset  - because must have self.object
    form_class = AlbumForm
    template_name = 'album-edit.html'
    context_object_name = 'album'
    success_url = reverse_lazy('home')


class AlbumDeleteView(views.DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    template_name = "album-delete.html"

    context_object_name = 'album'
    success_url = reverse_lazy('home')

    # to fill form with instance
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    #     disabled fields to delete form
    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        self.object.delete()
        return redirect(self.success_url)
