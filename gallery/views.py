from django.shortcuts import get_object_or_404
from .models import Art
from django.views.generic import (ListView, TemplateView,
                                  DetailView)


class ArtListView(ListView):
    templates_name = 'gallery/art_list.html'
    queryset = Art.objects.all()


class ArtDetailView(DetailView):
    template_name = "gallery/art_detail.html"
    # model = Art

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Art, id=id_)