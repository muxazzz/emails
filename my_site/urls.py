from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks', views.send, name='send'),
    path('list', views.send, name='lister'),
]