from . import views
from django.urls import path

app_name = 'abdullah'
urlpatterns = [
    path('home/', views.home, name='about'),
]