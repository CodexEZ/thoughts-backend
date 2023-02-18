from django.urls import path
from . import views

urlpatterns = [
    path('',views.getPosts),
    path('add/',views.createPost),
    path('register/',views.createUser),
    path('login/',views.userLogin)
]