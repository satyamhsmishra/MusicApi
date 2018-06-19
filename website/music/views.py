'''from django.shortcuts import render,get_object_or_404
from .models import Album,Song
def home(request):
    albums=Album.objects.all()
    context={'albums':albums}
    return render(request,'music/home.html',context)'''

'''def details(request,album_id):
    return HttpResponse("<h1>This album id is "+str(album_id)+ "</h1>")'''

'''def details(request,album_id):
   albums=get_object_or_404(Album,pk=album_id)
   context={'albums':albums}
   return render(request,'music/details.html',context)'''

'''def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,'music/details.html',{
    'album':album,
    'error_message':"You did not select a valid song",
    })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/details.html',{'album':album})'''

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from .models import Album

class IndexView(generic.ListView):
    template_name='music/home.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model=Album
    template_name='music/details.html'

class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model=Album
    success_url = reverse_lazy('music:home')


