from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index-home'),
    path('case/',views.case)
]
