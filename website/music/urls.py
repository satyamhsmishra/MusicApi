from django.urls import path
from . import views
app_name='music'

urlpatterns=[
    path('',views.IndexView.as_view(),name='home'),
    path('<pk>/', views.DetailsView.as_view(), name='details'),
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),
    path('album/<pk>/',views.AlbumUpdate.as_view() ,name='album-update'),
    path('album/<pk>/delete/',views.AlbumDelete.as_view(),name='album-delete'),
   # path('<int:album_id>/favorite/',views.favorite,name='favorite'),
]
