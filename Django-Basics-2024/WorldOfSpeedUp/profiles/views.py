from django.urls import reverse_lazy
from django.views import generic as views

from cars.models import Car
from common.views import get_profile
from profiles.forms import ProfileForm, ProfileEditForm
from profiles.models import Profile


# Create your views here.

class CreateProfileView(views.CreateView):
    form_class = ProfileForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('index')


class DetailsProfileView(views.DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()

    # TODO: simple
    def get_full_name(self):
        if self.object.first_name and self.object.last_name:
            return f'{self.object.first_name} {self.object.last_name}'
        elif self.object.first_name:
            return self.object.first_name
        elif self.object.last_name:
            return self.object.last_name
        return ""

    def get_total_price(self):
        cars_list = list(Car.objects.filter(owner=self.get_object().pk))
        total_price = sum([car.price for car in cars_list])

        return total_price

    def get_context_data(self, **kwargs):
        person = self.get_object()
        context = super().get_context_data(**kwargs)
        context["total_price"] = self.get_total_price()

        context["profile_name"] = self.get_full_name()

        return context


class EditProfileView(views.UpdateView):
    model = Profile  # or queryset  - because must have self.object
    form_class = ProfileEditForm
    template_name = 'profiles/profile-edit.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('details profile')

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
