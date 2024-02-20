from django.urls import path

from profiles.views import ProfileDetails, ProfileDeleteView

urlpatterns = [
    path('details/', ProfileDetails.as_view(), name='profile details'),
    path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
]
