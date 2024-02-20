from django.urls import path, include

from app.views import CreateAlbumView, AlbumDetailsView, AlbumDeleteView, AlbumEditView

urlpatterns = [
    path('add/', CreateAlbumView.as_view(), name='create album'),
    path('<int:pk>/', include([
        path('details/', AlbumDetailsView.as_view(), name='album details'),
        path('edit/', AlbumEditView.as_view(), name='album edit'),
        path('delete/', AlbumDeleteView.as_view(), name='album delete'),
    ])),
]
