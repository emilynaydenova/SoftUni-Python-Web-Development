from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from cars.forms import CarForm, CarDeleteForm
from cars.models import Car


# Create your views here.
class CreateCarView(views.CreateView):
    form_class = CarForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')


class DetailsCarView(views.DetailView):
    model = Car
    template_name = "cars/car-details.html"


class EditCarView(views.UpdateView):
    model = Car  # or queryset  - because must have self.object
    form_class = CarForm
    template_name = 'cars/car-edit.html'
    context_object_name = 'car'
    success_url = reverse_lazy('catalogue')


class DeleteCarView(views.DeleteView):
    model = Car
    form_class = CarDeleteForm
    template_name = "cars/car-delete.html"

    context_object_name = 'car'
    success_url = reverse_lazy('catalogue')

    # to fill form with instance
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    # #     disabled fields to delete form
    def form_invalid(self, form):

        self.object.delete()
        return redirect(self.success_url)
