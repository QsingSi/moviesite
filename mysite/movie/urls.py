from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('search/', views.search, name='search'),
        ]

