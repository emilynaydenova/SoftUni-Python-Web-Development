from django.urls import path, include

from cars.views import CreateCarView, DetailsCarView, EditCarView, DeleteCarView
from common.views import CatalogueView

urlpatterns = [
    path("catalogue/", CatalogueView.as_view(), name="catalogue"),
    path('create/', CreateCarView.as_view(), name="create car"),
    path('<int:pk>/', include([
        path('details/', DetailsCarView.as_view(), name='details car'),
        path('edit/', EditCarView.as_view(), name='edit car'),
        path('delete/', DeleteCarView.as_view(), name='delete car'),
    ]))
]
