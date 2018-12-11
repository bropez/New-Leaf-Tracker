from django.urls import path
from .views import (ArtListView, ArtDetailView)


app_name = 'gallery'
urlpatterns = [
    path('', ArtListView.as_view(), name='art-list'),
    path('<int:id>/', ArtDetailView.as_view(), name='art-detail'),
    # path('', TestView.as_view(), name='art-list'),
]
