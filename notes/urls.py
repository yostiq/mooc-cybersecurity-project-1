from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addnote/', views.addnote, name='addnote'),
    path('readnote/<int:noteid>', views.readnote, name='readnote'),
    path('deletenote/', views.deletenote, name='deletenote'),
]