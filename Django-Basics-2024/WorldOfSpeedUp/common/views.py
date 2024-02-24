from django.shortcuts import render

from cars.models import Car
from profiles.models import Profile
from django.views import generic as views

# Create your views here.

def get_profile():
    return Profile.objects.first()


class IndexView(views.TemplateView):
    template_name = "common/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile'] = get_profile()
        return context


class CatalogueView(views.ListView):
    queryset = Car.objects.all()
    template_name = "common/catalogue.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = get_profile()
        return context
