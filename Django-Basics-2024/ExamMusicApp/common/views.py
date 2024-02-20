from django.shortcuts import render
from django.urls import reverse_lazy

from albums.models import Album
from profiles.forms import ProfileForm
from profiles.models import Profile
from django.views import generic as views


def get_profile():
    return Profile.objects.first()


#
# def index(request):
#     profile = get_profile()
#     if profile:
#         context = {
#             'albums': Album.objects.all()
#         }
#         return render(request, 'home-with-profile.html', context)
#     else:
#         form = ProfileForm()
#         if request.method == 'POST':
#             form = ProfileForm(request.POST)
#             if form.is_valid():
#                 form.save()
#
#         context = {
#             'form': form,
#         }
#         return render(request, 'home-no-profile.html', context)


class IndexView(views.CreateView):
    model = Profile
    success_url = reverse_lazy('home')
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if get_profile():
            context['albums'] = Album.objects.all()
        return context

    def get_template_names(self):
        if get_profile() is None:
            return "home-no-profile.html"
        return "home-with-profile.html"
