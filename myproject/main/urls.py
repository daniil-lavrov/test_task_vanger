from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_page_view, name='home')
]