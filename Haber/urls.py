from django.urls import path
from . import views

urlpatterns = [
    path('get/',views.Haber, name='get'),
    path('tag/',views.Tag, name='tag'),
    
]