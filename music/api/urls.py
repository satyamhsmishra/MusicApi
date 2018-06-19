from django.urls import path
from .views import AlbumListAPIView,AlbumListCreateAPIView

urlpatterns = [
        path('',AlbumListAPIView.as_view(),name="listdetail"),
        path('create',AlbumListCreateAPIView.as_view(),name='create_api'),
]
