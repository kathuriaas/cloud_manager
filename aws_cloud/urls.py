from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='aws-cloud-home'),
    path('about/', views.about,name='aws-cloud-about'),
]
