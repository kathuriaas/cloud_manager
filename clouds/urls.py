from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='clouds-home'),
    path('about/', views.about,name='clouds-about'),
]
