from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='port'),
    path('port/', views.port, name='port'),

]