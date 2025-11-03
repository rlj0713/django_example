# '' → the empty string means this view is the home page
# views.section_list → calls the function we just defined
# name='section_list' → gives the URL a name, useful for links later

from django.urls import path
from . import views

urlpatterns = [
    path('', views.section_list, name='section_list'),
    path('create/', views.create_post, name='create_post'),
]
