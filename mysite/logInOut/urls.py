from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'login'
urlpatterns = [
        path('',auth_views.login, name='login'),
        ]
