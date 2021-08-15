from django.urls import path
from . import views

urlpatterns = [
    path('info-apiview/', views.InformationApiView.as_view()),
]