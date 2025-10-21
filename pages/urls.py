from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('about', views.about, name='about'),
]
