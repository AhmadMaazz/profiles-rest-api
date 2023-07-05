from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

# For ViewSet
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


# For APi Views
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
