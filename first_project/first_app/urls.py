from django.urls import path, re_path
from first_app import views

urlpatterns = [
    re_path(r'^index2$', views.index2),
    re_path(r'', views.index)
]
