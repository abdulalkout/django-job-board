
from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.Job_list ),
    path('job/',views.Job_detail),
]
