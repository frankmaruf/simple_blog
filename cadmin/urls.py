from django.urls import path
from . import views

urlpatterns = [
    path('post/add/', views.post_add, name ='post_add'),
]