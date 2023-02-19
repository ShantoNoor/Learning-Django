from django.urls import path, re_path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^index2$', views.index2, name='index2'),
    path('form/', views.form_input, name='form'),
    path('webform/', views.web_form, name='webform'),
]
