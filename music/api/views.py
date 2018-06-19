from django.db.models import Q
from .serializers import AlbumListSerializer
from rest_framework import generics,mixins #Mixins give the ability to ListView to create a user or data
from music.models import Album,Song

class AlbumListAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AlbumListSerializer
    # def get_queryset(self):
    #     qs = Album.objects.all()
    #     query = self.request.GET.get("q")
    #     if query is not None:
    #         qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    #     return qs
    queryset = Album.objects.all()  # Overrides attribute in GenericView

    def post(self,reqest,*args,**kwargs):      #  This method give the ability to ListAPIView create a new recoreds
        return self.create(reqest,*args,**kwargs)


class AlbumListCreateAPIView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = AlbumListSerializer





