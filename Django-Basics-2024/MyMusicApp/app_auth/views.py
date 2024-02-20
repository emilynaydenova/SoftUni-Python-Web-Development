from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from app_auth.forms import ProfileForm
from app_auth.models import Profile
from common.views import get_profile


# Create your views here.
class CreateProfile(views.CreateView):
    # model = Profile
    # fields = '__all__'
    form_class = ProfileForm
    template_name = 'home-no-profile.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = get_profile()
        return context


class ProfileDetails(views.DetailView):
    model = Profile
    template_name = 'profile-details.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = "profile-delete.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return get_profile()

