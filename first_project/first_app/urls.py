from django.urls import path, re_path
from first_app import views

urlpatterns = [
    path('', views.index),
    re_path(r'^index2$', views.index2),
    path('form/', views.form_input),
]
