from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('database/', views.database, name="demo"),
    path('database2/', views.database2, name="demo"),
    path('database3/', views.database3, name="demo"),
]
