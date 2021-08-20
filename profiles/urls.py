from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('info-viewset', views.InformationViewSet, basename='info-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('info-apiview/', views.InformationApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]